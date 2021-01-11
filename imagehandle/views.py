from django.shortcuts import render, redirect

# Create your views here.
from imagehandle.models import Student
from imagehandle.forms import CreateStudentForm

def StudentList(request):
	student=Student.objects.all().order_by('name')
	context={
		'student':student
	}
	return render(request, 'imagehandle/studentlist.html', context)

def CreateNewStudent(request):
	a=CreateStudentForm()
	if request.method=="POST":
		a=CreateStudentForm(request.POST, request.FILES)
		if a.is_valid():
			new=Student(
				name=a.cleaned_data['name'],
				roll_no= a.cleaned_data['roll_no'],
				image = a.cleaned_data['image']
				)
			new.save()
			return redirect('studentlist')

		else:
			a=CreateStudentForm()

	context={
		'a':a,
	}
	return render(request, 'imagehandle/createstudent.html', context)