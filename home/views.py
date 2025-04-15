from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def men(request):
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')

def kids(request):
    return render(request,'kids.html')

def appliances(request):
    return render(request,'appliances.html')