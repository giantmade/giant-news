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
- 