# from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import SignupForm 
from .models import Profile, Product

class ProfileSignupForm(SignupForm):

	def save(self, request):
		user = super(ProfileSignupForm, self).save(request)

		print("######################################")
		print("in custom signup form")
		print("######################################")
		print(user.email)
		profile = Profile(email=user.email,user=user)
		print("succeed")
		profile.save()

		return user