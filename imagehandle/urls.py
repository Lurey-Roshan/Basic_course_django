from django.urls import path
from imagehandle.views import StudentList, CreateNewStudent, deletestudent,studentDetail,editstudent
urlpatterns=[

	path('',StudentList,  name='studentlist'),
	path('createnewstudent', CreateNewStudent, name='createnewstudent' ),
	path('<int:pk>',studentDetail, name='studentdetail'),
	path('<int:pk>/delete', deletestudent, name='deletestudent'),
	path('<int:pk>/edit',editstudent, name='editstudent' ),

]	
 # if we want to import individual functions fromm view we do like below
 #from imagehandle.views import *
 #this statement imports everything from views.py
 # paths are defined as below
 #path('', views.StudentList,  name='studentlist'),