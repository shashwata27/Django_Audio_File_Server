from API.viewsets import SongViewset,PodcastViewset,AudiobookViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('song',SongViewset)
router.register('podcast',PodcastViewset)
router.register('audiobook',AudiobookViewset)