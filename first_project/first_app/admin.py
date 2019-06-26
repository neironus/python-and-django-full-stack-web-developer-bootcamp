from django.contrib import admin
from .models import Topic, WebPage, AccessRecord, User


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'category')
    list_display_links = ('name', 'url', 'category')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('top_name',)
    list_display_links = ('top_name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('first_name', 'last_name', 'email')

admin.site.register(Topic, TopicAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(AccessRecord)