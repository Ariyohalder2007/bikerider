from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('events/', views.events),
    path('contact/', views.contact),
    path('about/', views.about),
    path('event-read/<int:myid>', views.event_read),
]