from django.contrib import admin
from App_Attendance.models import Attendance, Department, Semester, Course

# Register your models here.
admin.site.register(Attendance)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Course)
