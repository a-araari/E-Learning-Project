from django.core.management.base import BaseCommand, CommandError

class OpenlabCommand(BaseCommand):

	def info(self, msg):
		self.stdout.write(msg)

	def success(self, msg):
		self.stdout.write(self.style.SUCCESS(msg))

	def warning(self, msg):
		self.stdout.write(self.style.WARNING(msg))

	def error(self, msg):
		self.stdout.write(self.style.ERROR(msg))