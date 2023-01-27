from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')


def gallary(request):
    return render(request, 'gallary.html')


def extra_services(request):
    return render(request, 'extra_services.html')


def facilities(request):
    return render(request, 'facilities.html')


def our_programs(request):
    return render(request, 'our_programs.html')

# About sub pages functions


def about_hcc(request):
    return render(request, 'about_hcc.html')


def whyhcc(request):
    return render(request, 'whyhcc.html')


def leadership(request):
    return render(request, 'leadership.html')


def ourstaff(request):
    return render(request, 'ourstaff.html')


def location(request):
    return render(request, 'location.html')


# Progarms sub pages functions (+2, school, BCA, Bsc.CSIT)

def plus2(request):
    return render(request, 'plus2.html')


def school(request):
    return render(request, 'school.html')


def bca(request):
    return render(request, 'bca.html')


def csit(request):
    return render(request, 'csit.html')

# Syllabus functions


def bca_syllabus(request):
    return render(request, 'bca_syllabus.html')


def csit_syllabus(request):
    return render(request, 'csit_syllabus.html')
