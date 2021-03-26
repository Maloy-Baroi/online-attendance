from django.contrib.auth.forms import forms
from App_Attendance.models import Attendance, Department, Course, Semester


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['student_id']


