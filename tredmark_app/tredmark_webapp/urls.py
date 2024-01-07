from django.urls import path
from . import views  #importing our view file 

urlpatterns = [
    path("", views.homepage, name="home"), #mapping the homepage function
    path("about", views.about, name="about"),
    path("appointment", views.appointment, name="appointment"),
    path("contact", views.contact, name="contact"),
    path("price", views.price, name="price"),
    path("service", views.service, name="service"),
    path("team", views.team, name="team"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("register", views.register_request, name="register"),
]
