from django.shortcuts import render, get_object_or_404 
from .models import Blog
from .forms import BlogForm
from django.shortcuts import redirect

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_list')