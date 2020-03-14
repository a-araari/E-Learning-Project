from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class OpenlabUserCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		]
