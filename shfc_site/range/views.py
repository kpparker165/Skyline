from django.template import Context, loader
from events.models import Event
from range.models import RangeShooting
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  page_content = RangeShooting.objects.latest('creation_date')
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

# def index(request):
#     return render(request, "range/index.html")
