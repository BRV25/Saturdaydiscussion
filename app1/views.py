from django.shortcuts import render
from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name="home.html"
     
class aboutpage(TemplateView):
    template_name="about.html"
     
