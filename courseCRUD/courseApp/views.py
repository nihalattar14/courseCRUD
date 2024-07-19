from django.shortcuts import render, redirect
from courseApp.forms import courseForm
from courseApp.models import Course

# Create your views here.

def getCourse(request):
    cources = Course.objects.all()
    return render(request,'courseApp/index.html',{'cources':cources})

def createCourse(request):
    form = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'courseApp/createCourse.html',{'form':form})

def deleteCourse(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')

def updateCourse(request,id):
    course = Course.objects.get(id=id)
    form = courseForm(instance = course)
    if request.method == 'POST':
        form = courseForm(request.POST,instance=form)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'courseApp/updateCourse.html',{'form':form})