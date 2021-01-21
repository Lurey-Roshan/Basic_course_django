from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
# Create your views here.
from .forms import SignupForm,UpdateUser,UpdateProfile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def signup(request):
	form=SignupForm()
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context={
	'form':form
	}

	return render(request, 'registration/register.html', context)

@login_required(login_url='login')
def myprofile(request):
	user=request.user
	profile, created=UserProfile.objects.get_or_create(pk=user.id)
	context={
		'profile':profile,
		'user':user

	}
	return render(request,'registration/profile.html', context)



@login_required(login_url='login')
def updateprofile(request):
	user=request.user
	update_user=UpdateUser(instance=user)
	profile, created=UserProfile.objects.get_or_create(pk=user.id)
	update_profile=UpdateProfile(instance=profile)
	if request.method=="POST":
		update_user=UpdateUser(request.POST, instance=user)
		update_profile=UpdateProfile(request.POST, request.FILES, instance=profile)
		if update_user.is_valid() and update_profile.is_valid():
			update_user.save()
			update_profile.save()
			return redirect('myprofile')
		else:
			print("invalid Format")
			update_user=UpdateUser(instance=user)
			update_profile=UpdateProfile(instance=user)
	context={
		'update_user':update_user,
		'update_profile':update_profile

	}
	return render(request, 'registration/update.html', context)

