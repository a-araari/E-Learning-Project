from django.urls import path, include
from . import views


app_name = 'courses'

urlpatterns = [
	path('', views.CourseList.as_view(), name='list'),
	path('mycourses/', views.MyCourseList.as_view(), name='my_courses'),
	path('create/', views.course_create, name='create'),

	path('<str:course_slug>/', include([
			path('', views.course_detail, name='detail'),
			path('update/', views.course_update, name='update'),
			path('delete/', views.course_delete, name='delete'),
			path('chapters/', views.chapter_list, name='chapter_list'),
			path('chapters/create/', views.chapter_create, name='chapter_create'),
			path('chapters/<str:chapter_slug>/',include(([
					path('', views.chapter_detail, name='detail'),
					path('update/', views.chapter_update_info, name='update_info'),
					path('update/content/', views.chapter_update_content, name='update_content'),
					path('delete/', views.chapter_delete, name='delete'),
				], app_name), namespace='chapter')
	),
		])
	),


]