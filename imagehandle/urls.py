from django.urls import path
from imagehandle.views import StudentList, CreateNewStudent
urlpatterns=[

	path('',StudentList,  name='studentlist'),
	path('createnewstudent', CreateNewStudent, name='createnewstudent' )
]
