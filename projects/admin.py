from django.contrib import admin
from .models import Project,Update
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','is_public')
    list_editable = ('is_public',)
    list_filter = ('title','description')
    search_fields = ['title','description']
    readonly_fields = ('date_created', 'date_updated')

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('status','is_update')
    list_editable = ('is_update',)
    list_filter = ('status','is_update')
    search_fields = ['status','is_update']
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Project,ProjectAdmin)
admin.site.register(Update,UpdateAdmin)