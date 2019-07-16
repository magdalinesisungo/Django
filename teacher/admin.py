from django.contrib import admin

# Register your models here.

from.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	list_display = ("id_number","first_name","last_name","email","date_employed","proffesion")
	search_fields= ("id_number","first_name","last_name","email","date_employed","proffesion")

admin.site.register(Teacher,TeacherAdmin)

