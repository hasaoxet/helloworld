from os import terminal_size
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homepageView(request):
    return HttpResponse("Hello world from Django!!!")

class HomepageView(TemplateView):
    template_name='home.html'

class AboutpageView(TemplateView):
    template_name='about.html'