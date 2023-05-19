from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,'home/notes.html')   
        else:
            return render(request,'login/signin.html')
    return render(request,'login/signin.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenum = request.POST.get('phone')
        my_user = User.objects.create_user(uname,email,password) 
        my_user.save()
        return render(request,'login/signin.html')
    return render(request,'login/reg.html')