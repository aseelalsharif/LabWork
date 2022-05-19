from django.shortcuts import render
from . models import Blog
# Create your views here.
def Blogg(request):
    #this function make copy from the blog and save it in th Post
    Post=Blog.objects.all()
    return render(request, 'Blog/blog.html',{'Post': Post})