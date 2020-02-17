from django.contrib import admin
from choonz.models import Playlist, Page, UserProfile

# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'playlist', 'url')

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)