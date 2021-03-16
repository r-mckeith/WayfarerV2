from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('posts/', views.posts_index, name="posts_index"),
  path('posts/<int:post_id>/', views.post_show, name="post_show"),
  path('posts/new/', views.post_new, name="post_new"),
  path('cities/', views.cities_index, name='cities_index'),
  path('cities/<int:city_id>/', views.city_show, name='city_show'),
]