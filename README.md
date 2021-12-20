# Giant News

A re-usable package which can be used in any project that requires a generic `News` app. 

This will include the basic formatting and functionality such as model creation via the admin.

## Installation

To install with the package manager, run:

    $ poetry add giant-news

You should then add `"news", "easy_thumbnails" and "filer"` to the `INSTALLED_APPS` in your settings file. 
The detail pages in this app use plugins which are not contained within this app. It is recommended that you include a set of plugins in your project, or use the `giant-plugins` app.

In order to run `django-admin` commands you will need to set the `DJANGO_SETTINGS_MODULE` by running

    $ export DJANGO_SETTINGS_MODULE=settings

## Configuration

This application exposes the following settings:

- `ARTICLETAG_ADMIN_LIST_DISPLAY` is the field list for the admin index. This must be a list
- `ARTICLETAG_ADMIN_FIELDSETS` allows the user to define the admin fieldset. This must be a list of two-tuples
- `ARTICLETAG_ADMIN_READONLY_FIELDS` allows the user to configure readonly fields in the admin. This must be a list

- `ARTICLE_ADMIN_LIST_DISPLAY`is the field list for the admin index. This must be a list
- `ARTICLE_ADMIN_SEARCH_FIELDS` allows the user to configure search fields in the admin. This must be a list
- `ARTICLE_ADMIN_FIELDSETS` allows the user to define the admin fieldset. This must be a list of two-tuples
- `ARTICLE_ADMIN_READONLY_FIELDS` allows the user to configure readonly fields in the admin. This must be a list

- `AUTHOR_ADMIN_LIST_DISPLAY`  is the field list for the admin index. This must be a list
- `AUTHOR_ADMIN_FIELDSETS` allows the user to define the admin fieldset. This must be a list of two-tuples
- `AUTHOR_ADMIN_READONLY_FIELDS` allows the user to configure readonly fields in the admin. This must be a list

- `RELATED_ARTICLES_LIMIT` allows the user to set how many articles are pulled through in the related articles plugin, the default is 3. Must be an int

## Sitemap
In order to add published articles to your sitemap, import the sitemaps file and add it to your `sitemaps` dict. This is usually contained within the main `urls.py` file.

## URLs

Add the following to `core.urls` for general functionality:

    path("news/", include("news.urls"), name="news"),

If you want to customize the urls to include a different path and/or templates, first you must import `from news import views as news_views` in `core.urls` and then you could add the following:

    path("news/", news_views.ArticleIndex.as_view(template_name="news/index.html"), name="news-index"),
    path("news/<slug:slug>/", news_views.ArticleDetail.as_view(template_name="news/detail.html"), name="news-detail"),
 
 ## Preparing for release
 
 In order to prep the package for a new release on TestPyPi and PyPi there is one key thing that you need to do. You need to update the version number in the `pyproject.toml`.
 This is so that the package can be published without running into version number conflicts. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.
 
 ## Publishing
 
 Publishing a package with poetry is incredibly easy. Once you have checked that the version number has been updated (not the same as a previous version) then you only need to run two commands.
 
    $ `poetry build` 

will package the project up for you into a way that can be published.
 
    $ `poetry publish`

will publish the package to PyPi. You will need to enter the username and password for the account which can be found in the company password manager
