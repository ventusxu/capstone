# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	# Assume URL is unique for every product
	url 	= models.URLField(max_length=300,primary_key=True,unique=True)

	source 	= models.CharField(max_length=10, blank=False)
	name 	= models.CharField(max_length=200, blank=False)
	# price multiplied by 100 to avoid float
	price 	= models.PositiveIntegerField()
	picture	= models.URLField(max_length=300)
	# liked_users = models.ManyToManyField(Profile,blank=True,related_name='liked_users')

	def __str__(self):
		return self.source + ' ' + self.name

	def __repr__(self):
		return self.source + ' ' + self.name


class Profile(models.Model):
	REQUIRED_FIELDS 	= ('user',)
	USERNAME_FIELD 		= 'email'
	is_anonymous 		= False
	is_authenticated 	= True

	email 		= models.EmailField(unique=True)
	user 		= models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
	fav_list 	= models.ManyToManyField(Product,blank=True,related_name="liked_users")

	def __str__(self):
		return self.user.email

	def __repr__(self):
		return self.user.email
