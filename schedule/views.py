from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from datetime import date
import json

from .models import Calendar

def index(request):
    today = date.today()
    context = { 'today_ymd' : today.strftime('%Y-%m-%d') }
    if (request.user.id == None) :
        return redirect('/admin/login/?next=/schedule/')
    else :
        return render(request, 'schedule/index.html', context)
    
def get_events(request):
    if (request.user.id != None):
        data = list(Calendar.objects.filter(userId = request.user.id, start__gte = request.GET['start'][0:10], end__lte = request.GET['end'][0:10]).values())
        return JsonResponse(data, safe = False)
    else:
        return redirect('/admin/login/?next=/schedule/')

def set_all_day_event(request):
    if (request.user.id != None):
        data =  json.loads(request.body.decode('utf-8'))
        calendar = Calendar(userId = request.user.id, title = data['title'], start = data['start'], end = data['end'], allDay = data['allDay'])
        calendar.save()
        return JsonResponse({ "result" : "success", "eventId" : calendar.id }, safe = False)
    else:
        return redirect('/admin/login/?next=/schedule/')