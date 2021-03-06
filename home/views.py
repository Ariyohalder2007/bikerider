from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Event
import datetime
from django.core.mail import send_mail

tdate = datetime.date.today


def index(request):
    event = Event.objects.all()
    
    params={'Event':event, 'tday': tdate}
    return render(request, "home/index.html", params)
def search_event(request):
    event = Event.objects.all()
    
    
    params={ 'Event':event, 'tday':tdate}
    print(tdate)
    return render(request, "home/search_event.html", params)

def events(request):
    
    event = Event.objects.all()
    
    params={ 'Event':event, 'tday':tdate}
    return render(request, "home/events.html", params)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('Name','')
        email=request.POST.get('Email', '')
        phone=request.POST.get('Phone','')
        message=request.POST.get('Message', '')
        try:
            send_mail(
            'Bikerider contact message',
            f"Phone: {phone} \n Message: {message}",
            email,
            ['alokhalder6359@gmail.com'],
            fail_silently=False,
            ) 
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/')  
            
        return HttpResponseRedirect('/')  
        
    return render(request, "home/contact.html")

def event_read(request, myid):
    event=Event.objects.get(id=myid)
    params={'event':event}
    # print(event)

    return render(request, "home/event_read.html", params)

def about(request):
    return render(request, "home/about.html")

def locate(request):
    return render(request, 'home/locate.html')

def search_com(request):
    if request.method=='GET':
        mydate=request.GET.get('mydate')
        # print(mydate)
        event=Event.objects.filter(event_date=mydate)
        
        params={
            'mydate':mydate,
            'Event':event
        }
        print(event)
        

        return render(request, 'home/search_com.html', params)
# Create your views here.
