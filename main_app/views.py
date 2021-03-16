from django.shortcuts import render, redirect
from .models import Post, City
from .forms import PostForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts})

def post_show(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/show.html', { 'post': post })

def post_new(request):
  post_form = PostForm(request.POST or None)
  if request.POST and post_form.is_valid():
    new_post = post_form.save(commit=False)
    new_post.user = request.user
    new_post.city_id = request.POST['cityId']
    new_post.save()
    return redirect('posts_index')
  else:
    return render(request, 'posts/new.html', { 'post_form': post_form })

def cities_index(request):
  return render(request, 'cities/index.html')

def city_show(request, city_id):
  post_form = PostForm(request.POST or None)
  city = City.objects.get(id=city_id)
  return render(request, 'cities/show.html', { 
    'city': city,
    'post_form': post_form
    })