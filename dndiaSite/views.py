from django.shortcuts import render
from django.shortcuts import redirect

def redirect_blog(request):
    return redirect ('home:index', permanent=True)


