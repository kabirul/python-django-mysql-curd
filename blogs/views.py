from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogForm
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request,'blogs/index.html',{'blogs':blogs} )
    #return HttpResponse("Hello, world. You're at the polls index.")

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/blogs/')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'blogs/create.html', {'form':form})

def update_blog(request,pk):
    blogs = Blog.objects.get(id=pk)
    form = BlogForm(instance=blogs)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/blogs/')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request,'blogs/update.html',context)

def delete_blog(request, pk):
    blogs = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/blogs/')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blogs/delete.html', context)
  
  
	   