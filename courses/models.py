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
		def get_updated_qs(slug):
			return self.objects.filter(slug=slug.lower()).order_by("-id")
		return create_slug(get_updated_qs(self.name), get_updated_qs, self.name)


class Chapter(models.Model):
	slug 		= models.SlugField()
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
		def get_updated_qs(slug):
			return self.course.chapter_set.filter(slug=slug.lower()).order_by("-id")

		return create_slug(get_updated_qs(self.name), get_updated_qs, self.name)

	def get_next_index(self):
		if self.course.chapter_set:
			return len(self.course.chapter_set.all()) + 1
		else:
			return 1


def create_slug(qs, get_updated_qs, name):
	name = name.replace(' ', '-').lower()
	slug = name
	count = 0

	while qs.exists():
		slug = f'{name}-{qs.count() + count}'

		count += 1
		qs = get_updated_qs(slug)

	return slug