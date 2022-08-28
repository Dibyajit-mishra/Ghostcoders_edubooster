from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Task']
            dm = fm.cleaned_data['description']
            reg = User(Task=nm, description=dm)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'assignapp/addandshow.html', {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request, id):
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            fm = StudentRegistration(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
            else:
                pi = User.objects.get(pk=id)
                fm = StudentRegistration(instance=pi)
        return render(request, 'assignapp/updatestudent.html',{'form':fm})