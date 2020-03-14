from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseList


urlpatterns = [
    path('', CourseList.as_view(), name='home'),
    path('about/', home_views.about, name='about'),
    path('contact/', home_views.contact, name='contact'),

    path('courses/', include('courses.urls')),

    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	