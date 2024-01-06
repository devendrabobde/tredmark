from django.shortcuts import render

# Create your views here.

def homepage(request):
  return render(request, 'index.html', context={})

def about(request):
  return render(request, 'about.html', context={})

def appointment(request):
  return render(request, 'appointment.html', context={})

def contact(request):
  return render(request, 'contact.html', context={})

def price(request):
  return render(request, 'price.html', context={})

def service(request):
  return render(request, 'service.html', context={})

def team(request):
  return render(request, 'team.html', context={})

def testimonial(request):
  return render(request, 'testimonial.html', context={})
