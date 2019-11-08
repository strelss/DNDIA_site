from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name ='index'),
    path('partners/', views.partners, name='partners'),
    path('papers/', views.papers, name='papers'),
    path('buklet/', views.buklet, name='buklet'),
]