# coding=utf-8
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
#    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='static/profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=128, null=True)
    summary = models.CharField(max_length=128, null=True)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)
    # picture = models.ImageField(upload_to = 'img')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return str(self.id)


class News(models.Model):  # 新闻表
    myurl = models.URLField(max_length=256, null=True)  # 来源
    picture = models.CharField(max_length=100, null=True)  # picture_path
    title = models.CharField(max_length=128, unique=True)  # 标题
    date = models.CharField(max_length=100, null=True)  # 生成时间
    summary = models.CharField(max_length=100, unique=True)  # 概要

    def __unicode__(self):
        return self.title
