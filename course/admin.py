from django.contrib import admin

# Register your models here.

from .models import Course


class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","duration_in_month","description")
	search_fields= ("name","duration_in_month","description")

admin.site.register(Course,CourseAdmin)

