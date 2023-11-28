from django.shortcuts import render,redirect
from .models import *

from django import forms

class Edit(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


def home(request):
    c = Course.objects.all()
    return render(request,'index.html',{'c':c})


def s(request):
    if request.method == 'POST':
        s = request.POST.get('search')
        obj = Course.objects.filter(id__icontains=s) or Course.objects.filter(name__icontains=s)

    return render(request,'result.html',{'obj':obj})

def edit(req,id):
    form = Edit()
    s = Course.objects.get(pk=id)
    if req.method == 'POST':
        form = Edit(req.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = Edit()
    else:
        form = Edit(instance=s)
    
    return render(req, 'edit.html',{'form':form})


def delete_page(request):
    d = Course.objects.all()
    return render(request,'delete.html',{'de':d})


def delete(request):
     if request.method == 'POST':
        s = request.POST.get('delete')
        obj = Course.objects.get(id=s).delete()
        return redirect('/')