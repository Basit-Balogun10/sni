from django.contrib import admin

from blog.models import BlogPost, Like, Dislike, Comment, Reply, PostReport, CommentReport, ReplyReport

from django.db import models

from tinymce.widgets import TinyMCE

admin.site.register(Like)
admin.site.register(Dislike)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'comment_body', 'post', 'created_on', 'active', 'new')
    list_filter = ('active', 'created_on', 'commenter', 'comment_body', 'post', 'new')
    search_fields = ('commenter', 'comment_body')
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

# @admin.register(PostReport)
# class PostReportAdmin(admin.ModelAdmin):
#     list_display = ('reporter', 'title', 'post', 'created_on', 'new', 'reviewed', 'good', 'bad')
#     list_filter = ('title', 'reviewed', 'new', 'created_on', 'good', 'bad', 'reporter', 'post')
#     search_fields = ('title', 'post')
#     actions = ['seen', 'reviewed', 'good_report', 'bad_report', 'not_reviewed']

#     def seen(self, request, queryset):
#         queryset.update(new=False)


#     def reviewed(self, request, queryset):
#         queryset.update(reviewed=True)


#     def good_report(self, request, queryset):
#         queryset.update(good=True)
#         queryset.update(bad=False)
    
    
#     def bad_report(self, request, queryset):
#         queryset.update(bad=True)
#         queryset.update(good=False)


#     def not_reviewed(self, request, queryset):
#         queryset.update(reviewed=False)
#         queryset.update(good=False)
#         queryset.update(bad=False)


@admin.register(CommentReport)
class CommentReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'title', 'comment', 'created_on', 'new', 'reviewed', 'good', 'bad')
    list_filter = ('title', 'reviewed', 'new', 'created_on', 'good', 'bad', 'reporter', 'comment')
    search_fields = ('title', 'post')
    actions = ['seen', 'reviewed', 'good_report', 'bad_report', 'not_reviewed']

    def seen(self, request, queryset):
        queryset.update(new=False)


    def reviewed(self, request, queryset):
        queryset.update(reviewed=True)
        queryset.update(new=False)


    def good_report(self, request, queryset):
        queryset.update(good=True)
        queryset.update(bad=False)
        queryset.update(reviewed=True)
        queryset.update(new=False)
        for qs in queryset:
            qs.comment.active = False
            qs.comment.save()

    
    def bad_report(self, request, queryset):
        queryset.update(bad=True)
        queryset.update(good=False)
        queryset.update(reviewed=True)
        queryset.update(new=False)
        for qs in queryset:
            qs.comment.active = True
            qs.comment.save()


    def not_reviewed(self, request, queryset):
        queryset.update(reviewed=False)
        queryset.update(good=False)
        queryset.update(bad=False)

@admin.register(ReplyReport)
class ReplyReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'title', 'reply', 'created_on', 'new', 'reviewed', 'good', 'bad')
    list_filter = ('title', 'reviewed', 'new', 'created_on', 'good', 'bad', 'reporter', 'reply')
    search_fields = ('title', 'post')
    actions = ['seen', 'reviewed', 'good_report', 'bad_report', 'not_reviewed']

    def seen(self, request, queryset):
        queryset.update(new=False)


    def reviewed(self, request, queryset):
        queryset.update(reviewed=True)
        queryset.update(new=False)


    def good_report(self, request, queryset):
        queryset.update(reviewed=True)
        queryset.update(good=True)
        queryset.update(bad=False)
        queryset.update(new=False)
        for qs in queryset:
            qs.reply.active = False
            qs.reply.save()
    
    
    def bad_report(self, request, queryset):
        queryset.update(reviewed=True)
        queryset.update(bad=True)
        queryset.update(good=False)
        queryset.update(new=False)
        for qs in queryset:
            qs.reply.active = True
            qs.reply.save()


    def not_reviewed(self, request, queryset):
        queryset.update(reviewed=False)
        queryset.update(good=False)
        queryset.update(bad=False)

