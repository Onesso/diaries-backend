from django.contrib import admin
from .models import Blog
# Register your models here.

admin.site.register(Blog)
# from django.contrib import admin
# from .models import Blog
# # Register your models here.

# class NoteAdmin(admin.ModelAdmin):
#     list_display = ["title", "category", "created", "updated"]

# admin.site.register(Blog, NoteAdmin)