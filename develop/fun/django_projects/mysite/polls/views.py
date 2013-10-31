from django.http import HttpResponse, HttpResponseRedirect
# from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice

# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = Context({
#     #   'latest_poll_list': latest_poll_list,
#     #   })
#     # output = ', '.join([p.question for p in latest_poll_list])
#     # return HttpResponse(template.render(context))
#     return render(request, 'polls/index.html', {
#         'latest_poll_list': latest_poll_list,
#         })
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# def detail(request, poll_id):
#     # return HttpResponse("You're looking for %s" % poll_id)
#     # try:
#     #   poll = Poll.objects.get(pk=poll_id)
#     # except Poll.DoesNotExist:
#     #   raise Http404
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/details.html', {'poll': poll})
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/details.html'

# def results(request, poll_id):
#     # return HttpResponse("You're looking at the result of poll %s" % poll_id)
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll': poll})
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    # return HttpResponse("You're voting on poll %s" % poll_id)
    print "1"
    p = get_object_or_404(Poll, pk=poll_id)
    print "2"
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


