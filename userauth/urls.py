from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from userauth import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('loginn/',views.loginn),
    path('signup/',views.signup),
    path('logoutt/',views.logoutt),
    path('upload',views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_post),
    path('explore',views.explore),
    path('profile/<str:id_user>', views.profile, name='profile'),
    path('delete/<str:id>', views.delete),
    path('follow', views.follow, name='follow'),
    path('search-results/', views.search_results, name='search_results'),
]
