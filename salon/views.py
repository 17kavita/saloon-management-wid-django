from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from salon.models import Contact,UserSignup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc = request.POST.get('desc')

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request,"please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.error(request, "your message has been successfully send")


    return render(request,'contact.html')


def user_login(request):
    return render(request,'user_login.html')

def user_signup(request):

    if request.method == 'POST':
        fn = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']

        # if len(l) < 2 or len(f) or len(i)< 3 or len(e) < 10 or len(p) < 10 or len(gen)<6 or len(con)<10:
        #     messages.error(request, "please fill the form correctly")
        # else:
    usignup = UserSignup(fname=fn,lname=l, email=e, contect=con, gender=gen,image=i)
    usignup.save()
            # messages.error(request, "your message has been successfully send")
    return redirect('/user_signup')

    return render(request, 'user_signup.html')




def admin_login(request):
     if request.method=='POST':
         u = request.POST['uname']
         p = request.POST['pwd']
         user=authenticate(username=u,password=p)

         if user is not None:
             login(request,user)
             messages.success(request,"successfully logged in")
             return redirect('admin_home')
         else:
              messages.error(request, "Invalid Credentials,please try again")
              return redirect('admin_home')
     return render(request,'admin_login.html')

def admin_signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        p1 = request.POST.get('pwd')
        p2 = request.POST.get('cpwd')
        my_user=User.objects.create_user(uname,email,p1)
        my_user.save()
        return redirect('admin_login')
    return render(request, 'admin_signup.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    return render(request, 'admin_home.html')

def user_home(request):


    return render(request, 'user_home.html')

def Logout(request):
    if request.method=='POST':
        logout(request)
        messages.success(request, "successfully logged in")
        return redirect('user_login')
    return render(request, 'about.html')


