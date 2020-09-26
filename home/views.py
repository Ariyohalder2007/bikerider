from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
import datetime
mydate = datetime.date.today


def index(request):
    event = Event.objects.all()
    
    params={'Event':event, 'tday': mydate}
    return render(request, "home/index.html", params)


def events(request):
    
    event = Event.objects.all()
    
    params={'Event':event, 'tday':mydate}
    return render(request, "home/events.html", params)
def contact(request):
    
    return render(request, "home/contact.html")

def event_read(request, myid):
    event=Event.objects.get(id=myid)
    params={'event':event}
    # print(event)

    return render(request, "home/event_read.html", params)

def about(request):
    return render(request, "home/about.html")


# Create your views here.
