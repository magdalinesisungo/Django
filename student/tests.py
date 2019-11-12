from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Student
from student.forms import StudentForm
import datetime



class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name = "Magdaline",
            last_name = "Sisungo",
            date_of_birth = datetime.date(1998,6,10),
            gender = "female",
            registration_number = "1998",
            email = "mag.sisungo@gmail.com",
            phone_number = "0710464311",
            date_joined = datetime.date.today(),
            )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

    def test_age_is_always_above_17(self):
        self.assertFalse(self.student.clean() < 17 )

    def test_age_is_always_below_30(self):
        self.assertFalse(self.student.clean() > 30 )


class AddStudentTestCase(TestCase):
    def setUp(self):
        self.data = {
        "first_name": "Destiny",
        "last_name": "Magdaline",
        "date_of_birth": datetime.date(1996,9,4,),
        "gender": "Female",
        "registration_number": "3420",
        "email": "destinym.mag@gmail.com",
        "phone_number": "0746650027",
        "date_joined": datetime.date.today(),
        }

        self.bad_data ={
        "first_name": "Destiny",
        "last_name": "Magdaline",
        "date_of_birth": datetime.date(1996,9,4),
        "gender": "Female",
        "registration_number": "3456",
        "email": "destiny@gmail.com",
        "phone_number": "0746650027",
        "date_joined": "magda",
        }

    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertTrue(form.is_valid())


    def test_student_form_rejects_invalid_data(self):
        form = StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_student_view(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 302)

    def test_remove_student_view(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)