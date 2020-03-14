from django.db import models
from django.urls import reverse
from users.models import Teacher, Student


class Course(models.Model):
	slug 		= models.SlugField(unique=True)
	name 		= models.CharField(max_length=50)
	detail 		= models.CharField(max_length=250, verbose_name='About the course')
	thumbnail 	= models.ImageField(upload_to='courses/thumbnails/', null=True)

	teacher 	= models.ForeignKey(Teacher, on_delete=models.CASCADE)
	students 	= models.ManyToManyField(Student, related_name='students_to_course')

	created_date 		= models.DateTimeField(auto_now_add=True)
	last_update_date 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("courses:detail", kwargs={"course_slug": self.course.slug})

	def get_thumbnail_url(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			return '/media/courses/thumbnails/default.jpg'

	def get_slug(self):
		return create_slug(Course, self.name)


class Chapter(models.Model):
	slug 		= models.SlugField(unique=True)
	name 		= models.CharField(max_length=20)
	detail 		= models.CharField(max_length=250, verbose_name='About the chapter')
	content 	= models.TextField(null=True)
	index 		= models.IntegerField(default=1, null=False)

	course 		= models.ForeignKey(Course, on_delete=models.CASCADE)

	created_date		= models.DateTimeField(auto_now_add=True)
	last_update_date 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("courses:chapter:detail", kwargs={
				"course_slug": self.course.slug,
				"chapter_slug": self.slug
		    })

	def get_slug(self):
		return create_slug(Chapter, self.name)

	def get_next_index(self):
		if self.course.chapter_set:
			return len(self.course.chapter_set.all()) + 1
		else:
			return 1


def create_slug(model, name):
	name = name.replace(' ', '-').lower()
	slug = name

	if name is not None:
		slug = name

	qs = model.objects.filter(slug=slug).order_by("-id")

	if qs.exists():
		name = f"{slug}-{qs.first().id}"
		return create_slug(model, name=name)

	return slug
