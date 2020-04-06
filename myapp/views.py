from django.shortcuts import render
from . import models

def home(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    return render(request, 'home.html', {'search': search})
