from django.db.models.signals import pre_save, post_save
from.models import Course, Chapter
from django.dispatch import receiver


def pre_save_course(sender, instance, **kwargs):
	if instance.id is None:
		instance.slug = instance.get_slug()


def save_chapter(sender, instance, **kwargs):
	if instance.id is None:
		instance.slug = instance.get_slug()
		instance.index = instance.get_next_index()


pre_save.connect(pre_save_course, sender=Course)

pre_save.connect(save_chapter, sender=Chapter)


'''
	Signals to delete Thumbnails
	Signal on chapter delete to reorder the index
'''