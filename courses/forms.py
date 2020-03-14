from django import forms
from .models import Course, Chapter


class CourseCreateForm(forms.ModelForm):
	thumbnail = forms.ImageField(required=False)

	class Meta:
		model = Course
		fields = ('name', 'detail', 'thumbnail')


class CourseEditForm(forms.ModelForm):
	thumbnail = forms.ImageField(required=False)

	class Meta:
		model = Course
		fields = ('name', 'detail', 'thumbnail')


class ChapterCreateInfoForm(forms.ModelForm):

	class Meta:
		model = Chapter
		fields = ('name', 'detail', )


class ChapterEditInfoForm(forms.ModelForm):

	class Meta:
		model = Chapter
		fields = ('name', 'detail', )


class ChapterEditContentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.TextInput(), required=False)

	class Meta:
		model = Chapter
		fields = ('content',)
