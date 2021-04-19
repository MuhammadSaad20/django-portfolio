from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'var1':'Muhammad Saad',
        'var2':'21'
    }
    return render(request,'index.html',context)
    #return HttpResponse('this is HomePage')
def about(request):
    return render(request,'about.html')
    #return HttpResponse('this is AboutSection')


def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is services')

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been sent to admin!.')

    return render(request, 'contact.html')

    #return HttpResponse('this is contact')
