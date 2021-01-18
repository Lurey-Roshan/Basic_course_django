from django.shortcuts import render, redirect

# Create your views here.
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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
