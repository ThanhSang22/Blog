from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "pages/home.html")


def news(request):
    return render(request, "pages/news.html")


def khoahoc(request):
    return render(request, "pages/khoahoc.html")


def contact(request):
    return render(request, "pages/contact.html")


def error(request, exception):
    return render(request, "pages/error_404.html")
def error_500(request):
    return render(request, 'pages/home.html')