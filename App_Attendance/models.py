from django.db import models
from App_login.models import StudentInfo, TeacherInfo, CustomUser

course_choose = (
    ('CSE', 'Introduction to Computer System'),
    ('CSE', 'Programming Language'),
    ('CSE', 'Programming Language'),
    ('CSE', 'Physics (Electricity and magnetism)'),
    ('CSE', 'Differential Calculus and Co-Ordinate Geometry'),
    ('BBA', '')
)

course_code_choose = (
    ('CSE111', 'CSE111'),
)


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department}"


class Semester(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_in_semester')
    semester = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.department} {self.semester}"


class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester_in_courses')
    course_code = models.CharField(max_length=255)
    course = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_code}-{self.course}"


class Attendance(models.Model):
    # student_finding_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
    #                                          related_name='attendance_student_user')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_in_attendance')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester_in_attendance')
    section = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_in_attendance')
    shift = models.CharField(max_length=50)
    student_id = models.CharField(max_length=255, blank=True, null=False)
    teacher_id = models.CharField(max_length=255)
    submission_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    presence = models.BooleanField()
