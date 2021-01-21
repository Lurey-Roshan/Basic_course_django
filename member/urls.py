from django.urls import path
from .views import signup,myprofile,updateprofile

urlpatterns=[
		path('register',signup	, name='register'),
		path('my_profile',myprofile, name='myprofile'),
		path('myprofile/update', updateprofile, name='updateprofile'),
		
]