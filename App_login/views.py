from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.mail import message
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from App_login.forms import SignupForm, TeacherForm, StudentForm, TeacherQualificationForm
from App_login.forms import ProfilePictureChangeForm, UserProfileChangeForm
from App_login.models import TeacherQualification, CustomUser, StudentInfo, TeacherInfo


# Create your views here.
def signup_system(request):
    logout(request)
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            if (form.cleaned_data.get('is_student') == 1 and form.cleaned_data.get('is_teacher') == 1) or (
                    form.cleaned_data.get('is_student') == 0 and form.cleaned_data.get('is_teacher') == 0):
                return redirect('App_login:signup')
            else:
                form.save(commit=True)
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)  # True or False
                if user is not None:
                    login(request, user)
                    if form.cleaned_data.get('is_student') == 1:
                        return HttpResponseRedirect(reverse('App_login:student_sign'))
                    elif form.cleaned_data.get('is_teacher') == 1:
                        return HttpResponseRedirect(reverse('App_login:teacher_sign_1'))
    return render(request, "App_login/SignupForm.html", context={'form': form})


@login_required
def student_sys(request):
    student_form = StudentForm()
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            print(request.user)
            student = student_form.save(commit=False)
            student.student_user = request.user
            student.save()
            return HttpResponseRedirect(reverse('Home'))
    return render(request, "App_login/StudentForm.html", context={'student_form': student_form})


@login_required
def teacher_sys_1(request):
    teacher_qualification_form = TeacherQualificationForm()
    if request.method == 'POST':
        teacher_qualification_form = TeacherQualificationForm(request.POST)
        if teacher_qualification_form.is_valid():
            teacher_qualification = teacher_qualification_form.save(commit=False)
            teacher_qualification.Teacher_is = request.user
            teacher_qualification.save()
            return HttpResponseRedirect(reverse('App_login:teacher_sign_2'))
    return render(request, 'App_login/TeacherForm.html', context={'form': teacher_qualification_form})


@login_required
def teacher_sys_2(request):
    teacher_form = TeacherForm()
    print(request.user.id)
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, request.FILES)
        if teacher_form.is_valid():
            teacher = teacher_form.save(commit=False)
            teacher.teacher_user = request.user
            teacher.qualification = TeacherQualification.objects.all().get(Teacher_is__username=request.user)
            teacher.save()
            return HttpResponseRedirect(reverse('Home'))
    return render(request, 'App_login/TeacherForm2.html', context={'form': teacher_form})


def login_sys(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    diction = {'form': form}
    return render(request, 'App_login/login.html', context=diction)


@login_required
def logout_sys(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))


@login_required(login_url='App_Login:login')
def user_change(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChangeForm(instance=current_user)
    return render(request, "App_Login/change_profile.html", context={'form': form})


@login_required
def password_change(request):
    chng = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            chng = True
            return HttpResponseRedirect(reverse('App_main:profile'))
    return render(request, "App_Login/pass_change.html", context={'form': form, 'change': chng})


@login_required
def change_pro_pic(request):
    form = ProfilePictureChangeForm(instance=request.user)
    if request.method == 'POST':
        form = ProfilePictureChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:profile'))
    return render(request, "App_Login/add_profile_picture.html", context={'form': form})


def student_status(request):
    students = StudentInfo.objects.all()
    return render(request, "App_login/StudentStatus.html", {'students': students})


def faculty_status(request):
    teacher = TeacherInfo.objects.all()
    return render(request, 'App_login/Faculty_status.html', context={'teachers': teacher})
