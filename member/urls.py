from django.urls import path
from .views import signup

urlpatterns=[
		path('register',signup	, name='register')

]