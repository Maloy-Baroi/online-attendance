from django.urls import path
from App_login import views

app_name = 'App_login'

urlpatterns = [
    path('signup', views.signup_system, name='signup'),
    path('login', views.login_sys, name='login'),
    path('logout', views.logout_sys, name='logout'),
    path('teacher_sign/1', views.teacher_sys_1, name='teacher_sign_1'),
    path('teacher_sign/2', views.teacher_sys_2, name='teacher_sign_2'),
    path('student_sign', views.student_sys, name='student_sign'),
    path('edit_profile_picture', views.change_pro_pic, name='edit_profile_picture'),
    path('password_change', views.password_change, name='password_change'),
    path('user_change', views.user_change, name='user_change'),
    path('student-status', views.student_status, name='student_status'),
    path('teacher-status', views.faculty_status, name='teacher_status'),
]