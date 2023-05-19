from django.shortcuts import render
from .models import Message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        mail = request.POST.get("email")
        mess = request.POST.get("message")
        newMess = Message(name,mail,mess)
        newMess.save() 
    return render(request,'contact/contact us.html')