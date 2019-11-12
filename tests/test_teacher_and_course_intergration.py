import datetime
from django.test import TestCase
from teacher.models import Teacher
from course.models import Course




class TeacherCourseTestCase(TestCase):
    def setUp(self):
        self.teacher_a= Teacher.objects.create (
            first_name = "Magdaline",
            last_name = "Sisungo",
            date_of_birth = datetime.date(1998,6,10),
            gender = "female",
            id_number = "1998",
            email = "mag.sisungo@gmail.com",
            phone_number = "0710464311",
            date_employed = datetime.date.today(),
            )

        self.teacher_b = Teacher.objects.create (
            first_name = "Destiny",
            last_name = "Sisungo",
            date_of_birth = datetime.date(1998,6,10),
            gender = "female",
            id_number = "1998",
            email = "mag.destiny@gmail.com",
            phone_number = "0710464311",
            date_employed = datetime.date.today(),
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


    
	def test_course_can_be_trained_by_a_teacher(self):
       self.python.teacher = self.teacher_a
       self.assertEqual(self.python.teacher, self.teacher_a)
       self.java.teacher = self.teacher_a
       self.assertEqual(self.java.teacher, self.teacher_a)
       self.htmlcss.teacher = self.teacher_a
       self.assertEqual(self.htmlcss.teacher, self.teacher_a)


   def test_many_courses_can_be_trained_by_one_trainer(self):
       self.python.teacher = self.teacher_b
       self.java.teacher = self.teacher_b
       self.assertEqual(self.java.teacher,self.python.teacher,self.htmlcss.teacher)


