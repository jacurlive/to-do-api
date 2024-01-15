from django.contrib import admin
from .models import ToDo, Folder


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "completed", "user", "folder")
    list_display_links = ("id", "title")
    list_editable = ("completed", "folder")
    readonly_fields = ("user",)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
