from django.shortcuts import render, redirect , HttpResponseRedirect
from django.http import HttpResponse
from ExcelMail.models import Teacher_Feedback 
from teacher_Register.models import Teacher_signUp , Teacher_Register
from django.contrib.auth.models import User, auth
from django.contrib import messages
from teacher_Register.forms import TeacherRegisterFields    
from .form import Teacher_signUpFields
from displayData.views import teacher_Feedback , data

# Create your views here.
def index(request):
    return render(request, 'login.html')
    
def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid credential')
            return redirect("login")
    else:    
        return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        Teacher_Name = request.POST["UserName"]
        Password = request.POST['Password']
        if Teacher_signUp.objects.filter(UserName = Teacher_Name).exists():
            if Teacher_signUp.objects.filter(Password = Password).exists():
                context = data(Teacher_Name)
                return render(request,'FeedbackReport_user.html',context)
            messages.error(request,'username and password doesnot match')
            return redirect("login")
        messages.error(request,'username does not exist')
        return redirect("login")   
    return render("login")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Rpassword = request.POST['Rpassword']
        if password==Rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("login")
def reset(request):
    Teacher_signUp.objects.all().delete()
    Teacher_Register.objects.all().delete()
    Teacher_Feedback.objects.all().delete()
    messages.info(request,'items reset')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    


