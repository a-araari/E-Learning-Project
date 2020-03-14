from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	email = models.EmailField('email address', unique=True)
	username = models.CharField(max_length=30, unique=False)
	picture = models.ImageField(upload_to='users/pictures/', null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	def __str__(self):
		if self.is_student:
				type_ = 'Student'
		elif self.is_teacher:
			type_ = 'Teacher'
		elif self.is_superuser:
			type_ = 'Admin'
		else:
			type_ = 'None'
		return f'{type_}: {self.email}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.picture:
			pic = Image.open(self.picture.path)
			if pic.width > 256:
				pic.thumbnail((256, pic.height / (pic.width / 265)))
				pic.save(self.picture.path)


	def get_picture_url(self):
		if self.picture:
			return self.picture.url
		else:
			if self.is_student:
				return '/media/users/pictures/student-default.png'
			elif self.is_teacher:
				return '/media/users/pictures/teacher-default.png'
			else:
				return '/media/users/pictures/default.png'

	def get_picture_name(self):
		if self.picture:
			return self.picture.name 
		else:
			if self.is_student:
				return 'student.png'
			elif self.is_teacher:
				return 'teacher.png'
			else:
				return 'default.png'

	def get_profile(self):
		if self.is_student:
			return Student.objects.get(user=self)
		elif self.is_teacher:
			return Teacher.objects.get(user=self)
		else:
			return None

	def get_shortname(self):
		return f'{self.first_name[0:1]}.{self.last_name}'

	def get_fullname(self):
		return f'{self.first_name} {self.last_name}'

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	