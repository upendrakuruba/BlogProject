from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def Blogpage(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(is_published=True).order_by('posted_at')
    posts = Paginator(posts,3)
    page = request.GET.get('page')
    posts = posts.get_page(page)
    #print('10*--------',categories)
    context = {
        'categories':categories,
        'posts':posts
    }
    return render(request,'blog/blog.html',context)

@login_required(login_url='Login')
def Postpage(request,title):
    post = Post.objects.get(title=title)
    categories = Category.objects.all()
    categore = post.category
    related = Post.objects.filter(category=categore)
    comments = Comment.objects.filter(post=post)
    #print('10*--------',comments)
    recent = Post.objects.filter(is_published=True).order_by('posted_at')
    context = {
        'post':post,
        'categories':categories,
        'comments':comments,
        'recent':recent,
        'related':related,
    }
    return render(request,'blog/post.html',context)

@login_required(login_url='Login')
def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        post_id = request.POST.get('id')
        #print('10*---------',post_id,name)
        post = Post.objects.get(id=post_id)
        c = Comment(comment=comment,name=name,email=email,website=website,post=post)
        c.save()
        return redirect('Postpage',title=post.title)
    
    return redirect('Blogpage')



def search_view(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        posts = Post.objects.filter(title__icontains=keyword)
        categories = Category.objects.all()
        print('10*--------',posts)
        context = {
            'categories':categories,
            'posts':posts
            }
    return render(request,'blog/blog.html',context)

@login_required(login_url='Login')
def get_category(request,cat):
    category = Category.objects.get(name=cat)
    posts = Post.objects.filter(category=category)

    categories = Category.objects.all()
    #print('10*-------',posts)
    context = {
            'categories':categories,
            'posts':posts,
        }
    return render(request,'blog/blog.html',context)

