from django.template import Context, loader
from events.models import Event
from home.models import Home
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  page_content = Home.objects.latest('creation_date')
  c = Context({
  'latest_event_list': latest_event_list,
  'page_content' : page_content,
  })

  return render(request, 'index.html', c)

