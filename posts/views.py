from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Hey create me </h1>")

def post_detail(request): #retrive
    # instance= Post.objects.get(id=2)
    instance = get_object_or_404(Post, id=2)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_details.html", context)

def post_list(request): #list_items
    queryset = Post.objects.all()
    context ={
        "object_list": queryset,
        "title":"List"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Heylo update me </h1>")

def post_delete(request):
    return HttpResponse("<h1>hey delete me </h1>")
