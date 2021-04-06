from django.contrib import admin
from API.models import Song,Podcast,Audiobook

class RegAdmin(admin.ModelAdmin):
    pass

admin.site.register(Song, RegAdmin)
admin.site.register(Podcast, RegAdmin)
admin.site.register(Audiobook, RegAdmin)
