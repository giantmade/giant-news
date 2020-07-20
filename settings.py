
SECRET_KEY = "giant-news"
DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3"}}
INSTALLED_APPS=[
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
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "news",
]
ROOT_URLCONF="news.tests.urls"
TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["news/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ],
            "loaders": ["django.template.loaders.app_directories.Loader",],
        },
    },
]
MIDDLEWARE=[
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]
SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True

LANGUAGES = [
    ('en-gb', 'English'),
]

# DEFAULT_LANGUAGE = 'en-gb'
