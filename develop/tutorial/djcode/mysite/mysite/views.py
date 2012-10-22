from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body><html>" % now
    # return HttpResponse(html)
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    # try:
    #     offset = int(offset)
    # except Exception, e:
    #     raise Http404()
    # dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    hour_offset = int(offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())

