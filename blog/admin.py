from django.contrib import admin

from blog.models import BlogPost, Like, Dislike, Comment, Reply

from django.db import models

from tinymce.widgets import TinyMCE

admin.site.register(Like)
admin.site.register(Dislike)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'body', 'post', 'created_on', 'active', 'new')
    list_filter = ('active', 'created_on', 'commenter', 'body', 'post', 'new')
    search_fields = ('commenter', 'body')
    actions = ['approve_comments', 'disapprove_comments', 'seen']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def disapprove_comments(self, request, queryset):
        queryset.update(active=False)

    def seen(self, request, queryset):
        queryset.update(new=False)


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('replier', 'body', 'comment', 'created_on', 'active', 'new')
    list_filter = ('active', 'created_on', 'replier', 'body', 'comment', 'new')
    search_fields = ('replier', 'body')
    actions = ['approve_replies', 'disapprove_replies', 'seen']

    def approve_replies(self, request, queryset):
        queryset.update(active=True)

    def disapprove_replies(self, request, queryset):
        queryset.update(active=False)

    def seen(self, request, queryset):
        queryset.update(new=False)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_published', 'date_updated')
    list_filter = ('title', 'author', 'category', 'date_published', 'date_updated')
    search_fields = ('title', 'body')

    formfield_overrides = {

        models.TextField: {'widget': TinyMCE()}

    }
