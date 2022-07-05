# Giant News

A re-usable package which can be used in any project that requires a generic `News` app.

This will include the basic formatting and functionality such as model creation via the admin.

Supported Django versions:

- Django 2.2, 3.2

Supported django CMS versions:

- django CMS 3.8, 3.9

> &#x26a0;&#xfe0f; For Django 2.x, use giant-news 0.x

> &#x26a0;&#xfe0f; Release 1.0.0-alpha.1 and above are NOT compatible with
> versions < 1 due to model name changes and a migration reset. Only upgrade to
> this version if you are aware of what changes need to be made

## Installation and Configuration

To install with the package manager, run:

    $ poetry add giant-news

You should then add `"giant_news", "easy_thumbnails" and "filer"` to the `INSTALLED_APPS` in your settings file.
The detail pages in this app use plugins which are not contained within this app. It is recommended that you include a set of plugins in your project, or use the `giant-plugins` app.

It is highly recommended that you override the base Article model at the start
of a project, even if you have no intention of immediately changing any fields.
Changing from a non-swappable model to a swappable model is difficult and will require migration
hacking.

```
# models.py

from giant_news.models import AbstractArticle


class Article(AbstractArticle):
    pass


# in admin.py

from django.contrib import admin
from giant_news.admin import ArticleAdmin
from .models import Article


admin.site.register(Article, ArticleAdmin)

```

When the migrations are created for this new model it will need some tweaking as
Django will not set this up to use swapper. To do this add the following lines to
the initial migration file (this will replace the hardcoded dependency on the
0002 migration from giant_news)

```
import swapper

class Migration...

    dependencies = [
        ...
        ('giant_news', '0001_initial'),
        swapper.dependency("giant_news", "Article"),
    ]
```
We also need to tell it run this migration before any other migration inside the
giant_news library as the model needs to be "swapped" before any relations are
created. You can do this with another line just under the `dependencies` list.

```
    run_before = [
        ('giant_news', '0002_relatedarticlecardplugin_relatedarticleplugin'),
    ]
```
Once you have created a model, and only AFTER you run migrations, you'll need to
point swapper to this new model. You can do this with the following setting:

    GIANT_NEWS_ARTICLE_MODEL = "appname.Article"


## Admin
By default, the admin for each of the models is not installed. This is so that you can register them as you need within your custom app. To do so add the following lines to your admin.py

```
from giant_news.admin import ArticleAdmin, TagAdmin, CategoryAdmin, AuthorAdmin
from giant_news.models import Article, Tag, Category, Author

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
```

## CMS App
By default this app is not registered as a CMS App. However if you wish to use the builtin CMS app simply add the following line of code to the settings file.

    REGISTER_NEWS_APP = True

## Sitemap

In order to add published articles to your sitemap, import the sitemaps file and add it to your `sitemaps` dict. This is usually contained within the main `urls.py` file.

## URLs

It is recommended that the application be added to a CMS page via the apphook. However, if you wish to hardcode the URL, you can do so by adding the following to your main `urls.py` file:

```

    path("news/", include("giant_news.urls"), name="news"),
```

If you want to customize the urls to include a different path and/or templates, first you must import `from giant_news import views as news_views` in `core.urls` and then you could add the following:

    path("news/", news_views.ArticleIndex.as_view(template_name="news/index.html"), name="index"),
    path("news/<slug:slug>/", news_views.ArticleDetail.as_view(template_name="news/detail.html"), name="detail"),

# Local development

## Getting setup

To get started with local development of this library, you will need access to poetry (or another venv manager). You can set up a virtual environment with poetry by running:

    $ poetry shell

Note: You can update which version of python poetry will use for the virtualenv by using:

    $ poetry env use 3.x

and install all the required dependencies (seen in the pyproject.toml file) with:

    $ poetry install


## Management commands

As the library does not come with a `manage.py` file we need to use `django-admin` instead. However, we will need to set our `DJANGO_SETTINGS_MODULE` file in the environment. You can do this with:  

    $ export DJANGO_SETTINGS_MODULE=settings

From here you can run all the standard Django management commands such as `django-admin makemigrations`.

## Testing

This library uses Pytest in order to run its tests. You can do this (inside the shell) by running:

    $ pytest -v

where `-v` is to run in verbose mode which, while not necessary, will show which tests errored/failed/passed a bit more clearly. 

## Preparing for release

In order to prep the package for a new release on TestPyPi and PyPi there is one key thing that you need to do. You need to update the version number in the `pyproject.toml`.
This is so that the package can be published without running into version number conflicts. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.

## Publishing

Publishing a package with poetry is incredibly easy. Once you have checked that the version number has been updated (not the same as a previous version) then you only need to run two commands.

    $ `poetry build`

will package the project up for you into a way that can be published.

    $ `poetry publish`

will publish the package to PyPi. You will need to enter the company username (Giant-Digital) and password for the account which can be found in the company password manager
