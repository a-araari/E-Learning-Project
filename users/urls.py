from django.urls import path
from users import views as users_views


urlpatterns = [
	path('teacher/<int:pk>/', users_views.teacher_profile, name='teacher_profile'),
	path('student/<int:pk>/', users_views.student_profile, name='student_profile'),

	path('profile/', users_views.profile, name='profile'),
	path('login/', users_views.login, name='login'),
	path('logout/', users_views.logout, name='logout'),
	path('signup/', users_views.signup, name='signup'),
	path('signup/student/', users_views.student_signup, name='student_signup'),
	path('signup/teacher/', users_views.teacher_signup, name='teacher_signup'),
	path('change_password/', users_views.change_password, name='change_password'),
	path('reset/done/', users_views.password_reset_complete, name='password_reset_done'),
]