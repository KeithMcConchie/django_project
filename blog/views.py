from django.shortcuts import render

posts = [
    {'author': 'Keith',
    'title': 'first post',
    'content': 'first post content',
    'date_posted': 'August 27, 2018'
    },
    {'author': 'Kevin',
    'title': 'second post',
    'content': 'second post content',
    'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})