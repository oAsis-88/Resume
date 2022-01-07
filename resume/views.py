from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ProgrammingLanguages


def index(request):
    knowledge = ProgrammingLanguages.objects.all()
    context = {'knowledge': knowledge}
    return render(request, 'resume/index.html', context)


def smiley(request):
    return render(request, 'smiley/smiley.html')
