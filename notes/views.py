from django.http import HttpResponse
from django.shortcuts import render
from .models import Note

def hello(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})