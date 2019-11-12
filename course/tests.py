from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Course
from course.forms import CourseForm
import datetime


class AddCourseTestCase(TestCase):
    def setUp(self):
        self.data = {
        "name":"Python",
        "duration_in_month":5,
        "end_date":datetime.date.today(),
        "description":"web developer",
        
        }
        self.bad_data = {
        "name":"Python",
        "duration_in_month":"12yrs",
        "end_date":datetime.date.today(),
        "description":"web developer",
        "teacher":"Mwai"
        }
    def test_course_form_accepts_valid_data(self):
        form = CourseForm(self.data)
        self.assertFalse(form.is_valid())

    def test_course_form_rejects_invalid_data(self):
        form = CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())


    def test_add_course_view(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 400)

    def test_remove_course_view(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)
# Create your tests here.








