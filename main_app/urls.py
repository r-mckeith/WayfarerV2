from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('posts/', views.posts_index, name="posts_index"),
  path('posts/<int:post_id>/', views.post_show, name="post_show"),
  path('cities/', views.cities_index, name='cities_index'),
]