# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	post=models.CharField(max_length=500)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	image=models.ImageField(upload_to='college_mate/media/post_image',blank=True)

class FinderStatus(models.Model):
	CHOICES=(
	('Available','Available'),
	('Nope','Not Available'),
	)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	apron = models.CharField(max_length=255,choices=CHOICES)
	created_date=models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = 'Apron Status'
		verbose_name_plural = 'Apron Status'

	# # def __str__(self):
	# 	return self.created_date



class FinderStatus2(models.Model):
	CHOICES=(
	('Available','Available'),
	('Nope','Not Available'),
	)
	drafter = models.CharField(max_length=255,choices=CHOICES)
	created_date=models.DateTimeField(default=timezone.now)



	class Meta:
		verbose_name = 'Drafter Status'
		verbose_name_plural = 'Drafter Status'
