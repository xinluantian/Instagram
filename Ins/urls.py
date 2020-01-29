"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path   //how to add include function
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))    //how to use include function
"""
from django.contrib import admin
from django.urls import include, path
from Ins.views import (HelloWorld, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike, UserDetailView)



urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name='HelloWorld'),
    path('', PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="post_delete"),
    path('like', addLike, name='addlike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
