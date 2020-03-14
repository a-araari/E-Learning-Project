from django.db.models.signals import post_save
from.models import User, Student, Teacher
from django.dispatch import receiver


def save_profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_student:
			student = Student(user=instance)
			student.save()
		elif instance.is_teacher:
			teacher = Teacher(user=instance)
			teacher.save()


post_save.connect(save_profile, sender=User)