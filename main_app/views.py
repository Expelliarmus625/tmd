from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
# Create your views here.


def home(request):
    form = ImageForm()
    return render(request, 'index.html', {'form': form})

