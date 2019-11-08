from django.urls import path

from . import views

app_name = 'progress'
urlpatterns = [
    path('work/', views.work, name ='work'),
    path('scientifpoten/', views.scienpot, name='scienpot'),
    path('matbase/', views.matbase, name='matbase')
]