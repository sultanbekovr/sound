from django.contrib import admin
from . import models

@admin.register(models.AuthUser)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'join_date')
    list_display_links = ('email', )

@admin.register(models.SocialLinks)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link',)
