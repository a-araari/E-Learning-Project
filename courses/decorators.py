from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib import messages
from courses.models import Course
from users.models import Teacher

def is_teacher(user):
	return user.is_authenticated and (user.is_teacher or user.is_superuser)

def teacher_required(func):

	def wrapper(request, *args, **kwargs):
		user = request.user

		if is_teacher(user):
			value = func(request, *args, **kwargs)
			return value
		
		raise PermissionDenied()

	return wrapper


def teacher_owner_required(func):

	def wrapper(request, course_slug, *args, **kwargs):
		user = request.user

		if is_teacher(user):
			course = get_object_or_404(Course, slug=course_slug)
			teacher = get_object_or_404(Teacher, user=user)

			if course.teacher == teacher:
				value = func(request, course_slug, *args, **kwargs)

				return value

		raise PermissionDenied()

	return wrapper