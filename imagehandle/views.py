from django.shortcuts import render

# Create your views here.
from imagehandle.models import Student

def StudentList(request):
	student=Student.objects.all().order_by('name')
	context={
		'student':student
	}
	return render(request, 'imagehandle/studentlist.html', context)