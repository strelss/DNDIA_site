from django.shortcuts import render

from .models import *

def work(request):
    i1 = Progress_Work1.objects.get()
    i2 = Progress_Work2.objects.get()
    i3 = Progress_Work3.objects.get()
    return render(request, 'progress/work.html', {'i1':i1, 'i2':i2, 'i3':i3})

def scienpot(request):
    i = Progress_Potencial.objects.get()
    return render(request, 'progress/scientifpoten.html', {'i':i})

def matbase(request):
    i = Progress_Matbase.objects.get()
    return render(request, 'progress/matbase.html', {'i':i})