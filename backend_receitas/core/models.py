# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    telephone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name.encode('utf-8')


class Ingredient(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name.encode('utf-8')


class Category(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name.encode('utf-8')


class Image(models.Model):
	image = models.ImageField(upload_to="media",default="media")

class Recipe(models.Model):
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 800)
	images = models.ManyToManyField(Image)
	category = models.ForeignKey('Category',on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient, through = "IngredientInRecipe")
	preparation_time = models.IntegerField(default = 1)
	preparation_instructions = models.CharField(max_length=1000, blank=True)
	portions = models.IntegerField(default = 1)
	nutritional_value = models.IntegerField(default = 1)
	cooking_method = models.CharField(max_length=30, blank=True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name.encode('utf-8')

class IngredientInRecipe(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	recipe = models.ForeignKey(Recipe)
	measure_unit = models.CharField(max_length=10, blank=True)
	quantity = models.IntegerField(default = 1)