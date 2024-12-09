from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.

admin.site.register(Tag)

class PostAmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAmin)