
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import User
from .forms import StudentResistration
# Create your views here.


#this function for add new and show
def add_show(request):
    if request.method == 'POST':
     fm = StudentResistration(request.POST)
     
     if fm.is_valid():
        nm= fm.cleaned_data['name']
        em= fm.cleaned_data['email']
        pm = fm.cleaned_data['password']
        reg = User(name =nm,email=em,password =pm)
        reg.save()
     fm = StudentResistration()
    else:
        fm = StudentResistration()
    stud = User.objects.all()
    
    return render(request,'addandshow.html',{'form':fm,'stu':stud})

#this function for udate and edit
def update_data(request,id):
    if request.method == 'POST':
      pi= User.objects.get(pk=id)
      fm = StudentResistration(request.POST,instance=pi)
      if fm.is_valid():
       fm.save()
      return HttpResponseRedirect('/')
    else:
     pi= User.objects.get(pk=id)
     fm = StudentResistration(instance=pi)
     
    return render(request,'updatestudent.html',{'form':fm})



# this function for delete 
def delete_data(request,id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')