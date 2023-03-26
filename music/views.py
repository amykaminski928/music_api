# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get_all_songs (request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True) 
    
    return Response (serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_by_id (request, pk): 
    try:
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Song.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
        