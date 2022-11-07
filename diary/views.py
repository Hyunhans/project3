from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'diary/index.html',
        {
            'posts' : posts
        }
    )

def practice(request):
    return render(
        request,
        'diary/practice.html'
    )

def practice_2(request):
    return render(
        request,
        'diary/practice_2.html'
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'diary/single_post_page.html',
        {
            'post' : post,
        }
    )