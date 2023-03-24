# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song

# Create your views here.

@api_view(['GET'])
def get_all_songs (request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True) 
    
    return Response (serializer.data)