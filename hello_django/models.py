from django.db import models
from django.contrib.auth.models import User
import datetime

class QuestionManager(models.Manager):
	def popular(self):
		return self.get_queryset().order_by('-rating')
	def new(self):
		return self.get_queryset().order_by('created')


class Profile(models.Model):
	user = models.OneToOneField(User)
	rating = models.IntegerField(default=0)
	avatar = models.ImageField(upload_to="/home/kirill/ask_kir/static")
	def __unicode__(self):
		return self.rating


class Question(models.Model):
	title = models.CharField(max_length=200, default="Title")
	text = models.TextField()
	author = models.ForeignKey(User)
	created = models.DateTimeField(default=datetime.datetime.now)
	rating  = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
	objects = QuestionManager()


class QLike(models.Model):
        voted = models.NullBooleanField(default=None)
        user = models.OneToOneField(User)
        question = models.ForeignKey(Question)
        def __unicode__(self):
               return self.user.username


class Answer(models.Model):
	author = models.ForeignKey(User)
        question = models.ForeignKey(Question)
	text = models.CharField(max_length=200)
	created = models.DateTimeField(default=datetime.datetime.now)
	rating = models.IntegerField(default=0)
        def __unicode__(self):
              return self.text
	objects = QuestionManager()


class ALike(models.Model):
        voted = models.NullBooleanField(default=None)
        user = models.OneToOneField(User)
        answer = models.ForeignKey(Answer)
        def __unicode__(self):
               return self.user.username

class Tags(models.Model):
        name = models.CharField(max_length=20, default="test_tag")
        question = models.ManyToManyField(Question)
        def __unicode__(self):
                return self.name

