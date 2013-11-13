from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    for category in category_list:
        category.url = encoded_url(category.name)
    context_dict = {'categories': category_list, 'pages': page_list}
    # Render the response and send it back!
    return render_to_response('rango/index.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = decoded_url(category_name_url)
    context_dict = {'category_name': category_name}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist, e:
        print e
    return render_to_response('rango/category.html', context_dict, context)

def about(request):
    # return HttpResponse('Rango says: Here is the about page! Return to <a href="/rango/">rango home page</a>')
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('rango/about.html', context_dict, context)

def encoded_url(url):
    return url.replace(" ", "_")

def decoded_url(url):
    return url.replace("_", " ")

@login_required
def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render_to_response('rango/add_category.html', {'form': form}, context)

@login_required
def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decoded_url(category_name_url)

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)

            cat = Category.objects.get(name=category_name)
            page.category = cat
            page.views = 0
            page.save()
            return category(request, category_name_url)
        else:
            print form.errors

    else:
        form = PageForm()
        print form.visible_fields

    return render_to_response('rango/add_page.html',
        {'form': form,
        'category_name_url': category_name_url,
        'category_name': category_name
        },
        context)

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors


    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered }, context )

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse('Your rango is disabled!')

        else:
            print 'Invalid login details: {0}, {1}'.format(username, password)
            return HttpResponse('Invalid login details!')

    else:
        return render_to_response('rango/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/rango/")

@login_required
def restricted(request):
    context = RequestContext(request)
    return render_to_response('rango/restricted.html', {}, context)




