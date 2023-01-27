"""projectm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from college import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('gallary/', views.gallary, name='gallary'),
    path('facilities/', views.facilities, name='facilities'),
    path('our_programs/', views.our_programs, name='our_programs'),
    path('extra_services/', views.extra_services, name='extra_services'),
    # about sub pages
    path('about_hcc/', views.about_hcc, name='about_hcc'),
    path('leadership/', views.leadership, name='leadership'),
    path('ourstaff/', views.ourstaff, name='ourstaff'),
    path('location/', views.location, name='location'),
    path('whyhcc/', views.whyhcc, name='whyhcc'),
    # programs sub pages
    path('plus2/', views.plus2, name='plus2'),
    path('school/', views.school, name='school'),
    path('bca/', views.bca, name='bca'),
    path('csit/', views.csit, name='csit'),
    # syllabus sub pages
    path('bca_syllabus/', views.bca_syllabus, name='bca_syllabus'),
    path('csit_syllabus/', views.csit_syllabus, name='csit_syllabus'),
]

# from cgitb import handler
# from django.contrib import admin
# from django.urls import path
# from siteone import views