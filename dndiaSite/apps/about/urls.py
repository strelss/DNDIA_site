from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('history/', views.history, name ='history'),
    path('team/', views.team, name='team'),
    path('activity/', views.activity, name='activity'),

]