from django.contrib import admin
from .models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile')
    list_display_links = ('pk', 'profile')


admin.site.register(Profile, ProfilesAdmin)