from django.contrib.auth.forms import UserCreationForm, forms, UserChangeForm
from App_login.models import StudentInfo, TeacherInfo, TeacherQualification, CustomUser


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture',
                  'is_student', 'is_teacher')


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfilePictureChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', ]


class StudentForm(forms.ModelForm):
    admission_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Date_of_Birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = StudentInfo
        exclude = ['student_user']


class TeacherForm(forms.ModelForm):
    joining_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = TeacherInfo
        exclude = ['teacher_user', 'qualification']


class TeacherQualificationForm(forms.ModelForm):
    University = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'University'}))

    class Meta:
        model = TeacherQualification
        exclude = ['Teacher_is']

    def __init__(self, *args, **kwargs):
        super(TeacherQualificationForm, self).__init__(*args, **kwargs)
        self.fields['University'].label = "Alumni"
