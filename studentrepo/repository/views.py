from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Oops !! invalid username and password")
            return redirect('/')





from .models import Upload
import datetime
def upload(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            email=request.user.get_username()
            title=request.POST['title']
            subtitle=request.POST['subtitle']
            Class=request.POST['class']
            stream=request.POST['stream']
            subject=request.POST['subject']
            url=request.POST['url']
            print(title,subtitle,Class,stream,subject,url)
            upload=Upload(email=email,title=title,subtitle=subtitle,Class=Class,stream=stream,subject=subject,url=url,date=datetime.datetime.now().strftime ('%Y-%m-%d'))
            upload.save()
            messages.info(request,"form submitted succesfully")
            return render(request,'upload.html')
        else:
            messages.info(request,"Please Login First")
            return redirect('/')

    else:
        return render(request,'upload.html')

def studymaterial(request):
    if request.method=='POST':
        Class=request.POST['class']
        stream=request.POST['stream']
        subject=request.POST['subject']
        study=Upload.objects.filter(Class=Class,stream=stream,subject=subject)
        print(Class)
        print(stream)
        print(subject)
        print(len(study))
        if (len(study)!=0):
            return render(request,'studymaterial.html',{'c':Class,'stream':stream,'s':subject,'study':study,'noitemsearched':False,'notfound':False,'found':True,'length':len(study)})
        else:
            print('no item to search')
            return render(request,'studymaterial.html',{'c':Class,'stream':stream,'s':subject,'study':study,'noitemsearched':False,'notfound':True})
    else:
        return render(request,'studymaterial.html',{'c':'IX','stream':'Nostream','s':'English','noitemsearched':True,'notfound':False})

def profile(request):
    email=request.user.get_username()
    study=Upload.objects.filter(email=email)
    if(len(study)!=0):
        return render(request,'profile.html',{'study':study,'notfound':False,'found':True,'length':len(study)})
    else:
        return render(request,'profile.html',{'notfound':True,'found':False,'length':0})

def delete(request,id):
    study=Upload.objects.filter(id=id)
    if(len(study)==1):
        study.delete()
        messages.info(request,"Deleted succesfully")
        return redirect('/profile')
    else:
        messages.info(request,"Error in deleting")
        return redirect('/profile')
       
        
