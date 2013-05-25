#coding=utf-8
from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(u'类别描述')

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(u'发布日期')
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=40, blank=True)
    tags = TaggableManager()
