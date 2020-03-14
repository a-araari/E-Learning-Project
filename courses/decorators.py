
def teacher_required(func):
	def wrapper(*args, **kwargs):

		value = func(*args, **kwargs)

		return value

	return wrapper


def teacher_owner_required(func):
	def wrapper(*args, **kwargs):

		value = func(*args, **kwargs)

		return value

	return wrapper


def chapter_belongs_to_course_required(func):
	def wrapper(*args, **kwargs):

		value = func(*args, **kwargs)

		return value

	return wrapper