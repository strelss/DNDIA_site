from django.urls import path

from . import views

app_name = 'send_massage'
urlpatterns = [
    path('contacts/', views.contactsView, name ='contacts'),
    path('good/', views.send, name='send')
]