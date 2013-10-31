from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # return HttpResponse('Rango says hello world! Here is <a href="./about/">about us.</a>')
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am from context!"}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    # return HttpResponse('Rango says: Here is the about page! Return to <a href="/rango/">rango home page</a>')
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('rango/about.html', context_dict, context)
