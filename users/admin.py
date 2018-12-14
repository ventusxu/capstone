# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Profile

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	pass

class ProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)