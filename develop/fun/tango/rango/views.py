from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hello world! Here is <a href="./about/">about us.</a>')

def about(request):
    return HttpResponse('Rango says: Here is the about page! Return to <a href="/rango/">rango home page</a>')
