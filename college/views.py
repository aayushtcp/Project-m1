from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Admission, Contact
from django.core.mail import send_mail
from django.contrib import messages
import re

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        my_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\','_','~','!']
        g= any(char.isdigit() for char in name)
        if name!="" and len(name)>4 and regex.search(name) == None and name!=r"\\" and len(name)<20 and g!=True:
            # print("Pass")regex.search(name) == None and name!=r"\\"
            contact = Contact(name=name,
                email=email, phone=phone, content = content)
            contact.save()
            send_mail(
            'Testing Mail',
            'Hey thank you for taking an appointment we will inform you shortly about time!',
            'therespawner69@gmail.com',
            [email],
            fail_silently=False,
            )
            messages.success(request,'Successfully Received')
            return render(request, 'contact.html', {'name': name})
        else:
            messages.info(request,'Please fill the form correctly')
            return redirect('contact')        
    else:
        return render(request, 'contact.html', {})


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
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        grade = request.POST['grade']
        my_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\','_','~','!']
        g= any(char.isdigit() for char in name)
        h= any(char in my_list for char in address)
        print(h)
        if name!="" and len(name)>4 and regex.search(name) == None and name!=r"\\" and len(name)<20 and g!=True and h!=True:
            # print("Pass")regex.search(name) == None and name!=r"\\"
            admission = Admission(name=name,
                        email=email, phone=phone, address=address,dob=dob, grade=grade)
            admission.save()
            messages.success(request,'Successfully Received')
            return render(request, 'plus2.html', {})
        else:   
            messages.info(request,'Please fill the form correctly')
            return redirect('plus2')
    else:   
        return render(request, 'plus2.html', {})
    
def school(request):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        grade = request.POST['grade']
        my_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\','_','~','!']
        g= any(char.isdigit() for char in name)
        h= any(char in my_list for char in address)
        print(h)
        if name!="" and len(name)>4 and regex.search(name) == None and name!=r"\\" and len(name)<20 and g!=True and h!=True:
            # print("Pass")regex.search(name) == None and name!=r"\\"
            admission = Admission(name=name,
                        email=email, phone=phone, address=address,dob=dob, grade=grade)
            admission.save()
            messages.success(request,'Successfully Received')
            return render(request, 'school.html', {})
        else:   
            messages.info(request,'Please fill the form correctly')
            return redirect('school')
    else:   
        return render(request, 'school.html', {})


def bca(request):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        grade = request.POST['grade']
        my_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\','_','~','!']
        g= any(char.isdigit() for char in name)
        h= any(char in my_list for char in address)
        print(h)
        if name!="" and len(name)>4 and regex.search(name) == None and name!=r"\\" and len(name)<20 and g!=True and h!=True:
            # print("Pass")regex.search(name) == None and name!=r"\\"
            admission = Admission(name=name,
                        email=email, phone=phone, address=address,dob=dob, grade=grade)
            admission.save()
            messages.success(request,'Successfully Received')
            return render(request, 'bca.html', {})
        else:   
            messages.info(request,'Please fill the form correctly')
            return redirect('bca')
    else:   
        return render(request, 'bca.html', {})


def csit(request):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        grade = request.POST['grade']
        my_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\','_','~','!']
        g= any(char.isdigit() for char in name)
        h= any(char in my_list for char in address)
        if name!="" and len(name)>4 and regex.search(name) == None and name!=r"\\" and len(name)<20 and g!=True and h!=True:
            # print("Pass")regex.search(name) == None and name!=r"\\"
            admission = Admission(name=name,
                        email=email, phone=phone, address=address,dob=dob, grade=grade)
            admission.save()
            messages.success(request,'Successfully Received')
            return render(request, 'csit.html', {})
        else:   
            messages.info(request,'Please fill the form correctly')
            return redirect('csit')
    else:   
        return render(request, 'csit.html', {})

# Syllabus functions


def bca_syllabus(request):
    return render(request, 'bca_syllabus.html')


def csit_syllabus(request):
    return render(request, 'csit_syllabus.html')
