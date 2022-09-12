## 0.1.2
- Combine author name fields into one
- Add Category model
- Update url to be more explicit
- Add str test for new model

## 0.1.2.1
- add read time

## 0.1.2.2
- Change URL property on Article model to a method to remove error when using "view on site" 

## 0.1.3
- Add related article plugin 

## 0.2.0
- Add settings and files for tests to be run outside of a django project

## 0.4
- Add categories to the default filtering form

## 0.5.1
- Add sitemap

## 1.0.0-alpha.1
- Refactor models.py into a directory
- Removed customisation options for admin classes. Inheritance is now the
  recommended customisation option
- Introduced AbsractArticle class and Article class to allow for more
  flexibility in the future. Article is now a swappable model. 
- Reset migrations
- Fixed current article being displayed on the related articles plugin

## 1.0.0-beta.4
- Don't register admin by default (added steps to README)
- Fix template syntax so it doesn't raise Invalid block tag
- Fix `verbose_name_plural` for Category model
- Change Placeholder name to `class-name_placeholder` for generic content

## 1.1.0-beta.4
- Don't register CMS app by default. Controlled through settings variable REGISTER_NEWS_APP.

## 1.1.1
- Add `name` as searchable field for TagAdmin

## 1.2/1.2.1
- Add `_default_author()` method to retrieve the first default author
- Allow Authors to be deleted without CASCADING all of the related articles. Achieved by providing
  a default_author method to SET_DEFAULT on the author foreignkey.
- Add `is_default` to Author model and expose in the admin

## 1.2.2
- Add `_default_author` to __all__ 