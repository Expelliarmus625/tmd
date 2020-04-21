from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from accounts.models import ImageCollector
# Create your views here.


def home(request):
    form = ImageForm()
    uploaded = ImageCollector.objects.filter(username = request.user.username).order_by('-created_at')[:5]
    return render(request, 'index.html', {'form': form, 'uploaded' : uploaded})

