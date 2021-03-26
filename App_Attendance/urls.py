from django.urls import path
from App_Attendance import views

app_name = 'App_Attendance'

urlpatterns = [
    path('', views.attendance_sys, name='attendance'),
]