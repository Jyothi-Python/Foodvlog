from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'registration.html')

def loginpage(request):
    return render(request,'login.html')

def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists!!!!')
                print("Username already taken...")
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                print("Successed...")
                return redirect('/')
        else:
            messages.info(request,'Password doesnt match')
            print("Password is not Matching....")
            return redirect('register')
        # return redirect('login')
    else:
        return render(request,'registration.html')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username,password=password)
                # request.session["uid"] = user.id
                if user is not None:
                    auth.login(request,user)
                    messages.info(request,'welcome')
                    return redirect('/')
                else:
                    messages.info(request,'Invalid username or password')
                    return redirect('loginpage')


        else:
            return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
