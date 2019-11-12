from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Teacher
from teacher.forms import TeacherForm
import datetime


class TeacherTestCase(TestCase):
    def setUp(self):
        self.teacher = Teacher(
            first_name = "Magdaline",
            last_name = "Sisungo",
            date_of_birth = datetime.date(1998,6,10),
            gender = "female",
            id_number = "1998",
            email = "mag.sisungo@gmail.com",
            phone_number = "0710464311",
            date_employed = datetime.date.today(),
            )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.teacher.first_name, self.teacher.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.teacher.last_name, self.teacher.full_name())

    def test_age_is_always_above_17(self):
        self.assertFalse(self.teacher.clean() )

    def test_age_is_always_below_30(self):
        self.assertFalse(self.teacher.clean() )


class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {
        "first_name": "Destiny",
        "last_name": "Magdaline",
        "date_of_birth": datetime.date(1996,9,4,),
        "gender": "Female",
        "id_number": "3420",
        "email": "destinym.mag@gmail.com",
        "phone_number": "0746650027",
        "date_joined": datetime.date.today(),
        
        }
        self.bad_data ={
        "first_name": "Destiny",
        "last_name": "Magdaline",
        "date_of_birth": datetime.date(1996,9,4),
        "gender": "Female",
        "id_number": "3456",
        "email": "destiny@gmail.com",
        "phone_number": "0746650027",
        "date_joined": "datetime"
        }

    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertFalse(form.is_valid())

    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())


    def test_add_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 400)

    def test_remove_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)



       