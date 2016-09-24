from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'category', 'slug', 'pub_date']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
