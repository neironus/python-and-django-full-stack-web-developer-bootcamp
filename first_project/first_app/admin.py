from django.contrib import admin
from .models import Topic, WebPage, AccessRecord


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'category')
    list_display_links = ('name', 'url', 'category')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('top_name',)
    list_display_links = ('top_name',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(AccessRecord)