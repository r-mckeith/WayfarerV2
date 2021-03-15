from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts})

def post_show(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/show.html', { 'post': post })

def cities_index(request):
  return render(request, 'cities/index.html')