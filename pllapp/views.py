from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template('pllapp/index.html')
    context = {}
    # return HttpResponse("Hello, world. You're at pllapp index.")
    return HttpResponse(template.render(context, request))

def pll(request):
    template = loader.get_template('pllapp/pll_designer.html')
    context = {}
    return HttpResponse(template.render(context, request))
