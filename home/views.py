from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home(request):
	context = {
		'title': 'Home',
		'home_active': 'active',
	}
	return render(request, 'home/home.html', context)


def about(request):
	context = {
		'title': 'About',
		'about_active': 'active',
	}
	return render(request, 'home/about.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'You feedback have been successfully submitted.')
			return redirect('home')
	else:
		form = ContactForm()

	if request.user.is_authenticated:
		user = request.user
		form.fields['full_name'].initial = f'{user.first_name} {user.last_name}'
		form.fields['from_email'].initial = user.email

	context = {
		'form': form,
		'title': 'Contact',
		'contact_active': 'active',
	}

	return render(request, 'home/contact.html', context)