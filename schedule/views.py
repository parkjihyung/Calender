from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import date
import json

from .models import Calendar

def index(request):
    today = date.today()
    context = { 'today_ymd' : today.strftime('%Y-%m-%d') }
    return render(request, 'schedule/index.html', context)

def get_events(request):
    #data = list(Calendar.objects.filter(start >= request['start'], end <= request['end']).values())
    data = list(Calendar.objects.filter(start__gte = request.GET['start'][0:10], end__lte = request.GET['end'][0:10]).values())
    return JsonResponse(data, safe = False)

def set_all_day_event(request):
    data =  json.loads(request.body.decode('utf-8'))
    calendar = Calendar(title = data['title'], start = data['start'], end = data['end'], allDay = data['allDay'])
    calendar.save()
    return JsonResponse({"result" : "success"}, safe = False)

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''