from django.shortcuts import render

from .models import *


def index(request):
    page_prev = Index_Page.objects.get()
    citat_prev = Index_Citation.objects.get()
    return render(request, 'home/index_home.html', {'page_prev': page_prev, 'citat_prev': citat_prev})


def partners(request):
    i = Home_Partners.objects.get()
    return render(request, 'home/partners.html', {'i': i})


def papers(request):
    papers = Home_BukletPapers.objects.all()
    return render(request, 'home/papers.html', {'papers': papers})

def buklet(request):
    buklet = Home_Buklet.objects.all()
    return render(request, 'home/buklet.html', {'buklet': buklet})
