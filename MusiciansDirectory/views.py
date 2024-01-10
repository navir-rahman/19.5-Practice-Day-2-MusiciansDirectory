from django.shortcuts import render
from Album.models import AlbumModel
from musician.models import MusicianModel
# Create your views here.

def home(request):
    return render(request, 'home.html', {"album" : AlbumModel.objects.all() , "musician": MusicianModel.objects.all()})