from django.shortcuts import render

# Create your views here.
# web/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
