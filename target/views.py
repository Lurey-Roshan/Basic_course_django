from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from target.models import Post
from target.forms import CreatePost, UpdatePost
# Create your views here.
def home(request):

	return render( request,'home.html')

def contact(request):
	return render(request, 'contact/contact.html')

def about_us(request):
	return render(request,'aboutus.html')


def post_index(request):
	post=Post.objects.all().order_by('title')
	context ={ 
		'post':post
		}
	return render(request, 'post/post_index.html',context)

def post_detail(request, pk):
	#post=Post.objects.get(pk=pk)
	post = get_object_or_404(Post, pk=pk)
	context ={ 
		'post':post
		}
	return render(request, 'post/postdetail.html',context)

def post_delete(request, pk):
	#post=Post.objects.get(pk=pk)
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('postindex')


def Createpost(request):
	form=CreatePost()
	if request.method=="POST":
		form=CreatePost(request.POST)
		if form.is_valid():
			form.save()
			return redirect('postindex')

		else:
			form=CreatePost()

	context={
		'form':form
	}
	return render(request, 'post/createpost.html', context)

def updatepost(request,pk):
	p=get_object_or_404(Post, pk=pk)
	form=UpdatePost(instance=p)
	if request.method=="POST":
		form=UpdatePost(request.POST, instance=p)
		if form.is_valid():
			form.save()
			return redirect('postdetail', pk)
	context={
		'p':p,
		'form':form
	}
	return render(request,'post/editpost.html', context)

