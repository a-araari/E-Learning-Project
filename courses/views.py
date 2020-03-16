from django.shortcuts import (
		render,
		redirect,
		get_object_or_404
	)
from .forms import (
		CourseCreateForm,
		CourseEditForm,
		ChapterCreateInfoForm,
		ChapterEditInfoForm,
		ChapterEditContentForm,
	)
from .decorators import (
		teacher_required,
		teacher_owner_required,
	)
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse
from users.models import Teacher
from .models import Course, Chapter


@login_required
@teacher_required
def course_create(request):
	if request.method == 'POST':
		form = CourseCreateForm(request.POST, request.FILES)

		if form.is_valid():
			course = form.save(commit=False)
			teacher = Teacher.objects.get(user=request.user)
			course.teacher = teacher
			course.save()
			messages.success(request, f'\'{course.name}\' created.')
			return redirect('courses:detail', course_slug=course.slug)
	else:
		form = CourseCreateForm()

	context = {
		'title': 'Create course',
		'form': form,
	}

	return render(request, 'courses/course_create.html', context)


class CourseList(ListView):
	model = Course
	paginate_by = 20

	def get_queryset(self, *args, **kwargs):
		return Course.objects.all().order_by('-created_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Courses'
		context['courses_active'] = 'active'
		return context

# Mixins...
class MyCourseList(ListView):
	model = Course
	paginate_by = 20

	def get_queryset(self, *args, **kwargs):
		teacher = Teacher.objects.get(user=self.request.user)
		return Course.objects.filter(teacher=teacher).order_by('-created_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'My courses'
		context['my_courses_active'] = 'active'
		return context


# @login_required
def course_detail(request, course_slug):
	course = get_object_or_404(Course, slug=course_slug)
	chapter_list = course.chapter_set.all()

	context = {
		'title': course.name,
		'course': course,
		'owner': course.teacher.user == request.user,
		'chapter_list': chapter_list,
	}

	return render(request, 'courses/course_detail.html', context)


@login_required
@teacher_owner_required
def course_update(request, course_slug):
	course = get_object_or_404(Course, slug=course_slug)

	if request.method == 'POST':
		form = CourseEditForm(request.POST or None,
					request.FILES or None,
					instance=course
				)

		if form.is_valid():
			form.save()
			messages.success(request, 'Course updated successfully.')
			return redirect('courses:detail', course_slug=course.slug)
	else:
		form = CourseEditForm(instance=course)

	context = {
		'title': 'Update course',
		'course': course,
		'form': form
	}

	return render(request, 'courses/course_update.html', context)


@login_required
@teacher_owner_required
def course_delete(request, course_slug):
	course = get_object_or_404(Course, slug=course_slug)

	if request.method == 'POST':
		delete = request.POST.get('confirm', None)
		if delete:
			course.delete()
			messages.success(request, 'Course deleted successfully.')
			return redirect('courses:my_courses')

	context = {
		'title': 'Delete course',
		'course': course
	}

	return render(request, 'courses/course_delete.html', context)


def chapter_list(request, course_slug):
	course = get_object_or_404(Course, slug=course_slug)
	chapter_list = course.chapter_set.all()
	context = {
		'title': course.name,
		'course': course,
		'chapter_list': chapter_list,
		'owner': course.teacher.user == request.user,
	}

	return render(request, 'chapters/chapter_list.html', context)


@login_required
@teacher_owner_required
def chapter_create(request, course_slug):
	course = get_object_or_404(Course, slug=course_slug)

	if request.method == 'POST':
		form = ChapterEditInfoForm(request.POST, request.FILES)

		if form.is_valid():
			chapter = form.save(commit=False)
			chapter.course = course
			chapter.save()
			messages.success(request, f'\'{chapter.name}\' chapter created.')

			return redirect('courses:chapter:update_content',
				course_slug=course.slug,
				chapter_slug=chapter.slug,
			)
	else:
		form = ChapterEditInfoForm()

	context = {
		'title': course.name,
		'course': course,
		'form': form,
	}

	return render(request, 'chapters/chapter_create.html', context)


def chapter_detail(request, course_slug, chapter_slug):
	course = get_object_or_404(Course, slug=course_slug)
	# Getting the chapter from course__chater_set, so no need for @decorators
	chapter = get_object_or_404(course.chapter_set, slug=chapter_slug)
	chapter_set = course.chapter_set

	context = {
		'title': course.name,
		'course': course,
		'chapter': chapter,
		'owner': course.teacher.user == request.user,
	}
	if chapter.index > 1:
		context['previous'] = chapter_set.get(index=chapter.index - 1).get_absolute_url()

	if chapter.index < chapter_set.all().count():
		context['next'] = chapter_set.get(index=chapter.index + 1).get_absolute_url()

	return render(request, 'chapters/chapter_detail.html', context)


@login_required
@teacher_owner_required
def chapter_delete(request, course_slug, chapter_slug):
	course = get_object_or_404(Course, slug=course_slug)
	chapter = get_object_or_404(course.chapter_set, slug=chapter_slug)

	if request.method == 'POST':
		delete = request.POST.get('confirm', None)
		
		if delete:
			chapter.delete()
			messages.success(request, 'Chapter deleted.')

			return redirect('courses:chapter_list', course_slug=course.slug)

	context = {
		'title': 'Delete chapter',
		'course': course,
		'chapter': chapter
	}

	return render(request, 'chapters/chapter_delete.html', context)


@login_required
@teacher_owner_required
def chapter_update_info(request, course_slug, chapter_slug):
	course = get_object_or_404(Course, slug=course_slug)
	chapter = get_object_or_404(course.chapter_set, slug=chapter_slug)

	if request.method == 'POST':
		form = ChapterEditInfoForm(request.POST or None,
				request.FILES,
				instance=chapter
			)
		
		if form.is_valid():
			chapter = form.save()
			messages.success(request, 'Chapter updated successfully.')
			return redirect('courses:chapter:detail',
						course_slug=course.slug,
						chapter_slug=chapter.slug,
					)

	else:
		form = ChapterEditInfoForm(instance=chapter)

	context = {
		'title': 'Update chapter',
		'course': course,
		'chapter': chapter,
		'form': form,
	}

	return render(request, 'chapters/chapter_update_info.html', context)


@login_required
@teacher_owner_required
def chapter_update_content(request, course_slug, chapter_slug):
	course = get_object_or_404(Course, slug=course_slug)
	chapter = get_object_or_404(course.chapter_set, slug=chapter_slug)

	if request.method == 'POST':
		form = ChapterEditContentForm(request.POST or None, instance=chapter)
		
		if form.is_valid():
			chapter = form.save()
			messages.success(request, 'Chapter updated successfully.')
			return redirect('courses:chapter:detail',
						course_slug=course.slug,
						chapter_slug=chapter.slug,
					)

	else:
		form = ChapterEditContentForm(instance=chapter)

	context = {
		'title': 'Update chapter',
		'course': course,
		'chapter': chapter,
		'form': form,
	}

	return render(request, 'chapters/chapter_update_content.html', context)
