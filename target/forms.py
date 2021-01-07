from django import forms

from target.models import Post

class CreatePost(forms.ModelForm):
	class Meta:
		model= Post
		#fields='__all__'
		fields=['title', 'body']
		widgets={
			'title':forms.TextInput(),
			'body':forms.TextInput()

		}


class UpdatePost(forms.ModelForm):
	class Meta:
		model=Post
		fields=['body']
		widgets	={
			'body':forms.TextInput()
		}
		