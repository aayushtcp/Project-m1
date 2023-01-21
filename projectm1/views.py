from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'conatct.html')


def gallary(request):
    return render(request, 'gallary.html')


def extra_services(request):
    return render(request, 'extra_services.html')


def facilities(request):
    return render(request, 'facilities.html')


def our_programs(request):
    return render(request, 'our_programs.html')
