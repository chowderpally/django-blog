from django.shortcuts import render


posts = [
    {
        'author': 'Teja',
        'title': 'post1',
        'content': 'First post content',
        'date_posted': 'Today'
    },
    {
        'author': 'Sai',
        'title': 'post2',
        'content': 'second post content',
        'date_posted': 'Yesterday'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
