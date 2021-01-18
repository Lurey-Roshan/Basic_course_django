from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from imagehandle.models import Student
from imagehandle.forms import CreateStudentForm,StudentEditForm

@login_required(login_url='login')
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
			messages.success(request,"New student Created Successfully")
			return redirect('studentlist')

		else:
			a=CreateStudentForm()

	context={
		'a':a,
	}
	return render(request, 'imagehandle/createstudent.html', context)
def studentDetail(request, pk):
	student=get_object_or_404(Student, pk=pk)
	context={
	'student':student
	}
	return render(request,'imagehandle/studentdetail.html', context)

def deletestudent(request, pk):
	student=get_object_or_404(Student, pk=pk)
	student.delete()
	messages.success(request," Student Deleted Successfully")
	return redirect('studentlist')

def editstudent(request, pk):
	student=get_object_or_404(Student, pk=pk)
	form=StudentEditForm(instance=student)
	if request.method == "POST":
		form=StudentEditForm(request.POST , request.FILES , instance=student)
		if form.is_valid():
	
			form.save()
			messages.success(request," Student Detail Updated Successfully")
			return redirect('studentdetail', pk )
		else:
			messages.error(request,'Student Detail Cannot be Updated')
			form=StudentEditForm(instance=student)
	context={
		'student':student,
		'form':form
	}

	return render(request,'imagehandle/editstudent.html', context)
