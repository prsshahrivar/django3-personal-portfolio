from django.shortcuts import render , get_object_or_404
from .models import MyBlog
# Create your views here.
def all_blogs(request):
    blogs = MyBlog.objects.all()
    return render(request ,'blog/all_blogs.html' , {'blogs': blogs})


def detail(request , blog_id):
    blog = get_object_or_404(MyBlog , pk = blog_id)
    return render(request ,'blog/detail.html' , {'blog' :blog } )


