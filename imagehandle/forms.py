from django import forms
from imagehandle.models import Student

class CreateStudentForm(forms.ModelForm):
	class Meta:
		model= Student
		fields=['name', 'roll_no','image']

class StudentEditForm(forms.ModelForm):
	class Meta:
		model= Student
		fields=['name', 'roll_no','image']

