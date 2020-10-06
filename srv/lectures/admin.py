from django.contrib import admin
from .models import Lecture, Article, Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('h2_title', 'h2_slug', 'body')
    search_fields = ('title', 'body',)


class SectionInline(admin.TabularInline):
    model = Section


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionInline,]
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title',)
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')


class ArticleInline(admin.TabularInline):
    model = Article


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    inlines = [ArticleInline,]
    list_display = ('title', 'slug', 'desc', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'desc')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')
