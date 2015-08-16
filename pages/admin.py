from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','text','date_updated')
    search_fields = ['title','text']
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Page, PageAdmin)