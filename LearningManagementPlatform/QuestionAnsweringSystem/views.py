from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student
from django.shortcuts import render
# Create your views here.

def index(request):

    ''' this function returns home page

    :returns HttpResponse: HomePage
    '''

    return render(request,"register.html")

def register(request):

    ''' this function takes user details as input and stores those student details in database

    :param request: Student Details like Username, Password , Email etc.

    :returns HttpResponse: Successful response if details are created successfully

    '''
    if request.method == "POST":
        if request.POST:
            data = request.POST
            try:
                student_obj = Student(
                    username = data['username'],
                    email = data['email'],
                    password = data['password'],
                    college = data['college'],
                    roll_number = data['roll_number'],
                    phone_number = data['phone_number'],
                    state = data['state'],
                    city = data['city'],
                    country = data['country']
                )
                student_obj.save()
                return HttpResponse("You have successfully Registered")
            except:
                raise Http404("Validation Error")
        else:
            raise Http404("Page not found.")
    else:
        raise Http404("{} not available".format(request.method))

