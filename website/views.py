from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cause(request):
    return render(request, "cause.html")

def gallery(request):
    return render(request, "gallery.html")

def news(request):
    return render(request, "news.html")

def contact(request):
    return render(request, "contact.html")