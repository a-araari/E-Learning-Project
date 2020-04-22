import os
from django.contrib.messages import constants as messages


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
            )
        )
    )


INSTALLED_APPS = [
    'home',
    'users.apps.UsersConfig',
    'courses.apps.CoursesConfig',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'login_required.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'openlab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'openlab.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# login required middleware
LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'admin:index',
    'admin:login',
    'admin:logout',
    'login',
    'logout',
    'signup',
    'teacher_signup',
    'student_signup',
    'change_password',
    'password_change',
    'password_change_done',
    'password_reset',
    'password_reset_done',
    'password_reset_confirm',
    'password_reset_complete',
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'    
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files (Pictures, Courses ..)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Message tags
MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# CKEditor
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'courses/content/images/')
CKEDITOR_RESTRICT_BY_USER = True

# CKEditor Config
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbar_Custom': [
            ['Save', 'NewPage', 'Templates', 'Preview'],
            ['CodeSnippet',],
            ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-'],
            ['Link'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'Iframe'],
            '/',
            ['Format', 'Font', 'FontSize'],
        ],

        'width': '100%',
        'height': '500px',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'autoGrow_minHeight': '100%',
        'autoGrow_minWidth': '100%',
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'codesnippet',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


"""
{
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
"""