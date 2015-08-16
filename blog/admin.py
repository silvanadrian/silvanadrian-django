from django.contrib import admin
from .models import Post, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','text','owner','is_public','date_updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['title','text']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
