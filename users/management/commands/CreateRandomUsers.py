from ._OpenlabCommand import OpenlabCommand
from users.models import User
import random

data = [
	'stain',
	'spray',
	'wasteful',
	'scoff',
	'nassir',
	'foulen',
	'ahmed',
	'fedi',
	'adema',
	'kanaird',
	'bristol',
	'bag',
	'annie',
	'tiler',
	'yearbook',
	'female',
	'bill',
	'prompt',
	'deimos',
	'seven',
	'tablet',
	'chewy',
	'ruin',
	'mortify',
	'fission',
	'protract',
	'visibly',
	'blunt',
	'tashing',
	'judge',
	'key',
	'pettiness',
	'calm',
	'odiferous',
	'baloo',
	'slashed',
	'slain',
	'taho',
	'discharge',
	'anatomy',
]


class Command(OpenlabCommand):

	emails = [
		'@gmail.com',
		'@yahoo.com',
		'@yandex.com',
		'@twitter.com',
		'@outlook.com',
	]

	def add_arguments(self, parser):
		parser.add_argument('max', type=int)
		parser.add_argument('type', type=str)

	def handle(self, *args, **options):
		max_user_count = options.get('max', len(data))
		user_type = options.get('type', 'random')

		for i in range(max_user_count):
			username = data[random.randint(0, len(data)-1)]
			em_pr = self.emails[random.randint(0, len(self.emails) - 1)]
			email = f'{username}{em_pr}'
			while len(User.objects.filter(email=email)) != 0:
				username += f'{random.randint(0, 9)}'
				email = f'{username}{em_pr}'
			self.info(f'{i+1}) Creating \'{email}\' user')
			first_name = username
			last_name = username[::-1]
			password = f'{first_name}00{first_name}'
			_user_type = user_type
			if user_type == 'student':
				is_student = True
				is_teacher = False
			elif user_type == 'teacher':
				is_student = False
				is_teacher = True
			elif user_type == 'random':
				is_student = random.randint(0, 1) == 0
				is_teacher = not is_student
				_user_type = 'student' if is_student else 'teacher'
			user = User(
					first_name=first_name,
					last_name=last_name,
					email=email,
					is_student=is_student,
					is_teacher=is_teacher,
				)
			user.set_password(password)
			user.save()
			self.success(f'	{_user_type} : \'{email}\' with Password = \'{password}\' have been created')

