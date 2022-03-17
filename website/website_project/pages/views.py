from django.shortcuts import render

#Views is the place where you handle all of your various web pages
# Create your views here.

def base_view(request, *args,**kwargs):
	return render(request, "base.html", {})

def about_view(request, *args,**kwargs):
	return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def services_view(request, *args, **kwargs):
	return render(request, "services.html", {})