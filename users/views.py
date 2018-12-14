# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Profile, Product
from django.http import HttpRequest

# Create your views here.
def profile(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(email=request.user.email)
		favourites = list(profile.fav_list.all().values().order_by('name'))
		counts = len(favourites)

		for item in favourites:
			item['price'] = "$"+str(item['price']/100)+"."+"{:0>2d}".format(item['price']%100)

		return render(request, "user_profile.html", {'favourites': favourites, 'counts': counts})
	else:
		return HttpRequest("You are not logged in!")