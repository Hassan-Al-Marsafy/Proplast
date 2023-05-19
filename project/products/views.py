from django.shortcuts import render

# Create your views here.
def choosetype(request):
    return render(request,'products/choosetype.html')

def industrial(request):
    return render(request,'products/industrial.html')

def commercial(request):
    return render(request,'products/commercial.html')