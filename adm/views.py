from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import *

# Create your views here.

urls_tasks = "заглушка1"
urls_results = "заглушка2"
def adminka (request):     
    return render (request, 'index.htm', context={'UrlsT':urls_tasks, 'UrlsR':urls_results})
     
     
class URL_Create (View):
    def get (self, request):
        form = NewURL()
        return render(request, 'admin/index.htm', context={'form': form})
        