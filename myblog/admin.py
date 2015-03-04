from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
    list_display = ('title', 'author', 'created_date', 'modified_date',)
    list_filter = ['modified_date', 'created_date']


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    list_display = ('name', 'description',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)