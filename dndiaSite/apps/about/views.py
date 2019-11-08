from django.shortcuts import render

from .models import *

def history(request):
    i = About_History.objects.get()
    head_line = i.head_line
    history_text = i.history_text
    img_history = i.img_history
    return render(request, 'about/history.html', {'i': i, 'head_line':head_line, 'history_text':history_text, 'img_history':img_history})

def team(request):
    i = About_Command.objects.get()
    return render(request, 'about/team.html', {"i":i})

def activity(request):
    i = About_Servise.objects.get()
    return render(request, 'about/activity.html', {'i':i})

