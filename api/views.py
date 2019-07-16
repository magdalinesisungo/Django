from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from student.models import Student

from .serializers import TeacherSerializer
from teacher.models import Teacher

from .serializers import CourseSerializer
from course.models import Course



# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer