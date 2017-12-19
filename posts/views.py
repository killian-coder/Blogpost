from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForms
from . models import Post

# Create your views here.

def post_create(request):
    form = PostForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        #message success
        return HttpResponseRedirect(instance.get_absolute_url())


    # if request.method == 'POST':
    #     print(request.POST.get("title",))
    #     print(request.POST.get("content" ))
    context ={
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_detail(request,id=None): #retrive
    # instance= Post.objects.get(id=2)
    instance = get_object_or_404(Post, id=id)
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

def post_update(request,id =None):
    instance = get_object_or_404(Post, id=id)
    form = PostForms(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_delete(request):
    return HttpResponse("<h1>hey delete me </h1>")
