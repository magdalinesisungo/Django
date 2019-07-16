from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.

from .forms import TeacherForm
from .models import Teacher


def add_teacher(request):
	if request.method=="POST":
		form=TeacherForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("list_teachers")

	else:
		form=TeacherForm()
	return render(request, "add_teacher.html",{"form":form})


def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request, "all_teachers.html", {"teachers":teachers})


def teacher_details(request, pk):
	teacher = Teacher.objects.get(pk = pk)
	return render(request, "teacher_details.html", {"teacher":teacher})

def edit_teacher(request, pk):
	teacher = Teacher.objects.get(pk = pk)
	if request.method=="POST":
		form = TeacherForm(request.POST, instance=teacher)
		if form.is_valid:
			form.save()
		return redirect("list_teachers")

	else:
		form=TeacherForm(instance=teacher)
	return render(request, "edit_teacher.html", {"form":form})







