from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category, Page

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
        pass
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

