
SECRET_KEY = "giant-news"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INSTALLED_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "easy_thumbnails",
    "filer",
    "mptt",
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "news",
]
ROOT_URLCONF = "news.tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["news/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en-gb', 'English'),
]