import datetime
from django.test import TestCase
from student.models import Student
from course.models import Course


class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a= Student.objects.create (
            first_name = "Magdaline",
            last_name = "Sisungo",
            date_of_birth = datetime.date(1998,6,10),
            gender = "female",
            registration_number = "1998",
            email = "mag.sisungo@gmail.com",
            phone_number = "0710464311",
            date_joined = datetime.date.today(),
            )


        self.student_b = Student.objects.create (
            first_name = "Destiny",
            last_name = "Magdaline",
            date_of_birth = datetime.date(2000,6,10),
            gender = "female",
            registration_number = "1020",
            email = "destiny@gmail.com",
            phone_number = "0746650027",
            date_joined = datetime.date.today(),
            )


        self.python= Course.objects.create (
            name= "python",
            duration_in_month = 4,
            end_date = datetime.date.today(),
            description = "web app",
            )

        self.htmlcss = Course.objects.create (
            name= "htmlcss",
            duration_in_month = 4,
            end_date = datetime.date.today(),
            description = "web design",
            )


        self.javascript= Course.objects.create (
            name= "javascript",
            duration_in_month = 4,
            end_date = datetime.date.today(),
            description = "web development",
            )


    def test_student_can_join_a_course(self):
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)
        self.student_a.courses.add(self.htmlcss)
        self.assertEqual(self.student_a.courses.count(), 2)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(), 3)


    def test_student_can_join_many_courses(self):
        self.student_b.courses.add(self.python, self.htmlcss, self.javascript)
        self.assertEqual(self.student_b.courses.count(), 3)



            




