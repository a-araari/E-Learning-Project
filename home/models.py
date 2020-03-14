from django.db import models


SUBJECT_CHOISES = [
	('sp', 'Site problem'),
	('aa', 'An advice'),
]


class Contact(models.Model):

	full_name = models.CharField(max_length=30, null=True, help_text='User full name')
	from_email = models.EmailField(null=False, help_text='Email address (required)')
	subject = models.CharField(max_length=5,
		choices=SUBJECT_CHOISES,
		default=SUBJECT_CHOISES[0][0],
		null=True,
		blank=True,
		help_text='Contact subject')
	content = models.TextField(null=False, help_text='Contact content (required)')
	date = models.DateField(auto_now_add=True)
	reviewed = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contacts"

	def __str__(self):
		st = f'from {self.from_email}'
		if self.subject:
			st += f' about {self.subject}'
		return st
