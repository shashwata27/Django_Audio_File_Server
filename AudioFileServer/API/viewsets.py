from rest_framework import viewsets
from . import models
from . import serializers

class SongViewset(viewsets.ModelViewSet):
    queryset=models.Song.objects.all()
    serializer_class=serializers.SongSerializer

class PodcastViewset(viewsets.ModelViewSet):
    queryset=models.Podcast.objects.all()
    serializer_class=serializers.PodcastSerializer

class AudiobookViewset(viewsets.ModelViewSet):
    queryset=models.Audiobook.objects.all()
    serializer_class=serializers.AudiobookSerializer