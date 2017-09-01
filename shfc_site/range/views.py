from django.template import Context, loader
from events.models import Event
from range.models import ShootingRangeDetail, RSOCalendar
from django.http import HttpResponse
from django.shortcuts import render
import json
import datetime
from django.core import serializers


def index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  page_content = ShootingRangeDetail.objects.latest('creation_date')
  c = Context({
  'latest_event_list': latest_event_list,
  'page_content': page_content,
  })
  return render(request, 'range/index.html', c)

def home_index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  c = Context({
  'latest_event_list': latest_event_list,
  })
  return render(request, 'range/range_home.html',c)

def rso_calendar_data(request):
  rso_calendar_data = RSOCalendar.objects.all()

  json_res = []

  for record in rso_calendar_data:
    json_obj = dict(
          pk=record.pk, 
      rso_person_first=record.rso_person.first_name,
      rso_person_last=record.rso_person.last_name,
      rso_start_date=str(record.rso_start_date), 
      rso_end_date=str(record.rso_end_date),
        )
    json_res.append(json_obj)

  return HttpResponse(json.dumps(json_res), content_type="application/json")





