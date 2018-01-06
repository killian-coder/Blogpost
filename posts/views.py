from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForms
from . models import Post

# Create your views here.

def post_create(request):
    form = PostForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        #message success
        messages.success(request,"Post successsfuly Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Not Post successsfuly Created")

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
    queryset_list= Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list,10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
        #if page not interger
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context ={
        "object_list": queryset,
        "title":"List",
        "page_request_var": page_request_var,
    }
    return render(request, "index.html", context)


def post_update(request,id =None):
    instance = get_object_or_404(Post, id=id)
    form = PostForms(request.POST or None,request.FILES or None ,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Post updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "successfuly daleted")
    return redirect("posts:list")
