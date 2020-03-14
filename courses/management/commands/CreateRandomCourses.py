from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from courses.models import Course
from users.models import User, Teacher
from random import randint
from os import listdir, path
from pathlib import Path


class Command(BaseCommand):

	THUMBNAILS_BASE_DIR = path.join(Path(__file__).parent.absolute(), 'thumbnails')
	thumbnails = listdir(THUMBNAILS_BASE_DIR)

	courses_name = [
		'Java',
		'Python',
		'minecraft',
		'C-sharp',
		'C++',
		'C',
		'Kotlin',
		'HTML',
		'CSS',
		'Javascript',
		'PHP',
		'Bootstrap4'
	]

	def handle(self, *args, **kwargs):
		count = int(input(f'Courses count(max={len(self.courses_name)}): '))
		course_list = Course.objects.all()
		teacher_list = Teacher.objects.all()

		while count >= 0:
			name = self.courses_name[randint(0, len(self.courses_name) - 1)]
	
			if (not Course.objects.filter(name=name).exists()):
				self.stdout.write(self.style.SUCCESS(f'Creating \'{name}\' course..'))
				course = Course()
				course.name = name
				course.detail = f'Learning {name} in short period and become a developer'
				# thum = self.get_thumbnail(name)
				# course.tumbnail = ImageFile(open(thum, "rb"))

				course.teacher = teacher_list[randint(0, teacher_list.count() - 1)]

				course.save() 
				self.stdout.write(self.style.SUCCESS(f'\'{name}\' created/'))
			count -= 1
			
'''
	def get_thumbnail(self, name):
		name = name.lower()
		for thumbnail in self.thumbnails:

			if thumbnail.lower().startswith(name):
				return path.join(self.THUMBNAILS_BASE_DIR, thumbnail)
'''