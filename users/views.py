from django.shortcuts import render, redirect, get_object_or_404
from .forms import OpenlabUserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Student, Teacher, User
from courses.models import Course


def user_not_logged_in_required(func):

	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.warning(request, 'You are allready logged in!. Please, logout to continue.')

			return redirect('home')
		else:
			return func(request, *args, **kwargs)


	return wrapper


def teacher_profile(request, pk):
	teacher = get_object_or_404(Teacher, user_id=pk)
	course_list = Course.objects.filter(teacher=teacher)

	context = {
		'title': f'{teacher.user.get_shortname()}\'s profile',
		'teacher': True,
		'user_profile': teacher.user,
		'courses': course_list,
	}

	return render(request, 'registration/profile_show.html', context)


def student_profile(request, pk):
	student = get_object_or_404(Student, user_id=pk)
	context = {
		'title': f'{student.user.get_shortname()}\'s profile',
		'student': True,
		'user_profile': student.user,
	}

	return render(request, 'registration/profile_show.html', context)


@user_not_logged_in_required
def login(request):
	return LoginView.as_view()(request)


def logout(request):
	if not request.user.is_authenticated:
		return redirect('home')

	return LogoutView.as_view()(request)


@user_not_logged_in_required
def signup(request):
	context = {
		'title': 'Sign up',
	}

	return render(request, 'registration/signup.html', context)


@user_not_logged_in_required
def student_signup(request):
	form = OpenlabUserCreationForm()
	if request.method == 'POST':
		form = OpenlabUserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			user.is_student = True
			user.is_teacher = False
			user.save()
			messages.success(request, 'Your Student account have been created.')

			auth_login(request, user)

			next_ = request.POST['next'] or '/'
			next_ = '/' if next_ == request.path else next_

			return redirect(next_)
		else:
			messages.error(request, 'Wrong information, please try again!')
	context = {
		'form': form,
	}
	return render(request, 'registration/student_signup.html', context)


@user_not_logged_in_required
def teacher_signup(request):
	form = OpenlabUserCreationForm()
	if request.method == 'POST':
		form = OpenlabUserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			user.is_student = False
			user.is_teacher = True
			user.save()
			messages.success(request, 'Your Teacher account have been created.')

			auth_login(request, user)

			next_ = request.POST['next'] or '/'
			next_ = '/' if next_ == request.path else next_

			return redirect(next_)
		else:
			messages.error(request, 'Wrong information, please try again!')
	context = {
		'form': form,
	}
	return render(request, 'registration/teacher_signup.html', context)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	
	context = {
		'title': 'Password Change',
		'form': form
	}

	return render(request, 'registration/change_password.html', context)


# override the default PasswordRestComplete template view
def password_reset_complete(request):
    messages.success(request, 'Your password has been set. You may login now.')

    return redirect('login')


def profile(request):
	user = request.user
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		picture = request.FILES.get('picture')

		if first_name:
			user.first_name = first_name
		if last_name:
			user.last_name = last_name
		if picture:
			user.picture = picture
		if first_name or last_name or picture:
			user.save()
			messages.success(request, 'Information updated.')
		else:
			messages.warning(request, 'No changes detected.')

	context = {
		'title': 'Profile',
	}
	return render(request, 'registration/profile.html', context)

