from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"), #initial view on server
   path('about/',views.about, name="about"), 
   path('services/',views.services, name="services"), 
   path('contact/',views.contact, name="contact"), 
]
