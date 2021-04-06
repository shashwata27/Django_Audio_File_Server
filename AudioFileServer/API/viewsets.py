from rest_framework import viewsets,status
from . import models
from . import serializers
from rest_framework.response import Response

class SongViewset(viewsets.ModelViewSet):
    queryset=models.Song.objects.all()
    serializer_class=serializers.SongSerializer

class PodcastViewset(viewsets.ModelViewSet):
    queryset=models.Podcast.objects.all()
    serializer_class=serializers.PodcastSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AudiobookViewset(viewsets.ModelViewSet):
    queryset=models.Audiobook.objects.all()
    serializer_class=serializers.AudiobookSerializer