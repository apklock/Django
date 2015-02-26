from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from myblog.models import Author


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author, AuthorAdmin)
