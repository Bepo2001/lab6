from django.shortcuts import render,redirect
from django import forms
from .models import Student,Courses
from django.forms import ModelForm

class studentForms(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields='__all__'

def students(request):
    students = Student.objects.all()
    form = studentForms(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sql:students')
    return render(request, 'pageStyle/Student.html', {'students': students, 'form': form})

def courses(request):
    courses = Courses.objects.all()
    form = CourseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sql:courses')
    return render(request, 'pageStyle/Course.html', {'courses': courses, 'form': form})


def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    not_registered_courses = Courses.objects.exclude(courses_for_student=student)
    tcourse=student.courses.all
    if request.method == 'POST':
        course_id = request.POST.get('course')
        if course_id:
            course = Courses.objects.get(pk=course_id)
            student.courses.add(course)
            return redirect('sql:details', student_id=student_id)
    
    return render(request, 'pageStyle/Detail.html', {'student': student, 'course':tcourse,'not_registered_courses': not_registered_courses})

