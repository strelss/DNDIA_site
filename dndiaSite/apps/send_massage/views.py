from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Contact

def contactsView(request):
    return render(request, 'send_massage/contacts.html')

def send(request):
    a = Contact(contact_first_name = request.POST['fname'], contact_organization = request.POST['orgname'], contact_email = request.POST['email'], contact_massage = request.POST['message'])
    a.save()
    return render(request, 'send_massage/good.html')
