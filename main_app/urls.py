from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile_login, name="profile_login"),
  path('profile/<int:user_id>/', views.profile, name="profile"),
  path('profile/edit/', views.profile_edit, name="profile_edit"),
  path('posts/<int:post_id>/', views.post_show, name="post_show"),
  path('posts/new/', views.post_new, name="post_new"),
  path('cities/', views.cities_index, name='cities_index'),
  path('cities/<int:city_id>/', views.city_show, name='city_show'),
  path('accounts/signup/', views.signup, name='signup'),
] 