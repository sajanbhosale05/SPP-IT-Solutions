from django.shortcuts import render
from .models import Contact,Application

# Create your views here.
def index(request):
     return render(request,"index.html")

def career(request):
     return render(request,"careers.html")

def contact(request):
     if request.method == 'POST':
          name=request.POST.get('name')
          phone=request.POST.get('phone')
          email=request.POST.get('email')
          message=request.POST.get('message')
          try:
               Contact.objects.create(name=name, phone=phone,  email=email, message=message)

          except:
               print("Something went wrong..!!")
     return render(request,"index.html")

def application(request):
     if request.method == 'POST':
          name=request.POST.get('name')
          phone=request.POST.get('phone')
          email=request.POST.get('email')
          role=request.POST.get('status')
          experience=request.POST.get('experience')
          details=request.POST.get('details')
          resume=request.POST.get('fileToUpload')

          try:
               Application.objects.create(name=name,phone=phone,email=email,role=role,experience=experience,details=details,resume=resume)
          except:
               print("Something went Wrong....!!!!")
     return render(request,"index.html")

