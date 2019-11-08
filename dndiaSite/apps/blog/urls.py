from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name ='blog'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail_url'),
]