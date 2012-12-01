# Django settings for bl project.

DEBUG = False
TEMPLATE_DEBUG = True

ADMINS = (
    ('Olivier', 'olivier@lethanh.be')
    # ('Your Name', 'your_email@domain.com'),
)

ROOT = "/home/_WWW/www.cerkinfo.be/"
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cerkinfo',                      # Or path to database file if using sqlite3.
        'USER': 'phpBB',                      # Not used with sqlite3.
        'PASSWORD': 'jwcTmHmfEdfj',                  # Not used with sqlite3.
#        'NAME': 'test',                      # Or path to database file if using sqlite3.
#        'USER': 'phpBB',                      # Not used with sqlite3.
#        'PASSWORD': 'jwcTmHmfEdfj',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Brussels'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ROOT + 'ci.media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://www.cerkinfo.be/media/'

CKEDITOR_MEDIA_PREFIX = "/media/ckeditor/"
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + "uploads/"
CKEDITOR_UPLOAD_PREFIX = "/media/uploads/"

CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': [
			[ 'Source', 'Preview', '-', 'Bold', 'Italic', 'Underline','Strike'],
			['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
			'/',
			['NumberedList','BulletedList','Blockquote'],
			['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
			['Link','Unlink', 'Image','Flash','Table'],
			'/',
			['Styles','Format','Font','FontSize'],
			['TextColor','BGColor'],
			['Maximize', 'ShowBlocks']
			   ],
		'height': 300,
		'width': 600,
	},
}

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bho0r&^^y-p2r8h1t5-w&$++!8q=58456dhx&%u@7gy_f-ti)l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'ci.urls'

TEMPLATE_DIRS = (
    ROOT + "ci/templates",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
#    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'reversion',
    'flatblocks',
    'ci.rockypages',
    'ci.os',
    'ci.pv',
    'ci.memoires',
    'frontendadmin',
    'phpbb',
    'ci.fortunes',
    'django_extensions',
    'gcaltemplatetag',
)

# Added Phpbb backend
AUTHENTICATION_BACKENDS = (
    'phpbb.backends.PhpbbBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#Added context_processors.request for FrontEndAdmin
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)


# URL to your phpbb board
PHPBB_URL = "http://cerkinfo.be/phpbb/"

# URL to your phpbb board
PHPBB_SMILIES_URL = PHPBB_URL + "images/smilies/"

# Allow to map a PHPBB Group to a Django Group for permissions
# Must be a list of pair of id, Phpbb Group first.
# Ex : [(6,1), (2,3)]
PHPBB_GROUP_MAP = [(6,1), (624,2)]

PHPBB_NEWS_FORUM_ID = 20

# Front end admin conf
FRONTEND_FORMS = {
    'flatpages.flatpage': 'ci.rockypages.forms.FlatPageSimpleForm',
    'flatblocks.flatblock': 'ci.rockypages.forms.FlatBlockSimpleForm',
}
FRONTEND_FIELDS = {
#    'flatpages.flatpage': ['content'],
#    'flatblocks.flatblock': ['content'],
}
#FRONTEND_EXCLUDES = {
#'flatpages.flatpage': ('url'),
#    'flatpages.flatpage': ('title', 'sites', 'url', 'enable_comments', 'template_name', 'registration_required'),
#    }

