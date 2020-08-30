from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student
from django.shortcuts import render, redirect
# Create your views here.

def index(request):

    ''' this function returns home page

    :returns HttpResponse: HomePage
    '''

    return render(request,"register.html")

def login_page(request):

    ''' this function returns home page

     :returns HttpResponse: Login page
     '''
    return render(request, "login.html")

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

def login(request):
    '''
    This function takes login credentials as parameters and returns a response upon successfully logged in.
    :param request: rollnumber and password
    :return: HttpResponse upon successful authentication
    '''
    if request.POST:
        data = request.POST
        all_obj = Student.objects.all()
        for each_obj in all_obj:
            if str(each_obj.roll_number) == str(data['roll_number']):
                if str(each_obj.password) == str(data['password']):
                    return HttpResponse("You have successfully logged in")

        return redirect("login_page")

    else:
        raise Http404("{} not available".format(request.method))







