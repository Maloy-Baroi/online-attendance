from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
    "Enter a valid international mobile phone number starting with +(country code)"))
gender_choice = (
    ("male", "Male"),
    ("Female", "Female"),
    ("Third Gender", "Third Gender")
)


# Create your models here.
class CustomUser(AbstractUser):
    is_student = models.BooleanField(blank=True, default=1)
    is_teacher = models.BooleanField(blank=True, default=1)
    profile_picture = models.ImageField(upload_to='photos/profile_picture')


# Student
class StudentInfo(models.Model):
    student_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='Student')
    student_mobile_number = models.CharField(validators=[phone_regex], verbose_name=_("Student's Mobile phone"),
                                             max_length=17,
                                             blank=True, null=True)
    fathers_name = models.CharField(max_length=100)
    fathers_nid = models.IntegerField(unique=False)
    fathers_mobile_number = models.CharField(validators=[phone_regex], verbose_name=_("Father's Mobile phone"),
                                             max_length=17,
                                             blank=False, null=False)
    mothers_name = models.CharField(max_length=100)
    mothers_nid = models.IntegerField(unique=False)
    mothers_mobile_number = models.CharField(validators=[phone_regex], verbose_name=_("Mother's Mobile phone"),
                                             max_length=17,
                                             blank=False, null=False)
    Department = models.CharField(max_length=100)
    admission_date = models.DateField()
    student_id = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    Date_of_Birth = models.DateField(blank=False)
    gender = models.CharField(choices=gender_choice, max_length=15)
    batch = models.CharField(max_length=50)
    section_type = models.CharField(max_length=20)
    shift_type = models.CharField(max_length=100)

    class Meta:
        unique_together = ["student_id", "batch"]

    def __str__(self):
        return f"{self.student_id}-{self.student_user.first_name} {self.student_user.last_name}"


# Teacher
class TeacherQualification(models.Model):
    Teacher_is = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher_qualification_user')
    University = models.CharField(max_length=254, null=True)
    Subject = models.CharField(max_length=254, null=True)
    Qualification = models.CharField(max_length=254, null=True)
    passing_year = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Qualification} {self.Subject} {self.University}"


class TeacherInfo(models.Model):
    teacher_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher', default=-1)
    teacher_id = models.CharField(max_length=255)
    qualification = models.ForeignKey(TeacherQualification, on_delete=models.CASCADE)
    joining_date = models.DateField()
    Mobile_number = models.CharField(validators=[phone_regex], verbose_name=_("Teacher's Mobile phone"),
                                     max_length=17,
                                     blank=False, null=False)
    dept_name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    gender = models.CharField(choices=gender_choice, max_length=15)
    Major_subject_type = models.CharField(max_length=50)

