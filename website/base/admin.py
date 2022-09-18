from django.contrib import admin

from .models import *



class MetaDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_liked']

admin.site.register(Video)
admin.site.register(MetaData)
