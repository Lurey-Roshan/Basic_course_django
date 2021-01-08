from django.urls import path
from imagehandle.views import StudentList
urlpatterns=[

	path('',StudentList,  name='studentlist'),
]
