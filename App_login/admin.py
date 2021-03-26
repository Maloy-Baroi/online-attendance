from django.contrib import admin
from App_login.models import StudentInfo, TeacherInfo, CustomUser, TeacherQualification
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher', 'profile_picture')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher', 'profile_picture')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StudentInfo)
admin.site.register(TeacherQualification)
admin.site.register(TeacherInfo)
