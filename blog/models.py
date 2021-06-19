from datetime import timedelta

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

from tinymce.models import HTMLField


def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
    return file_path

def author_img_upload_location(instance, filename):
    file_path = 'author_img/{post_detail}/{author_id}-{filename}'.format(
        post_detail=str(instance.title) + '-' + str(instance.id), author_id=str(instance.author.id), filename=filename)
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_posts")
    author_img = models.ImageField(upload_to=author_img_upload_location, null=False, blank=False)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='liked', editable=False)
    disliked = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='disliked', editable=False)
    CATEGORIES = (("history", "HISTORY"), ("politics-and-international-relations", "POLITICS & INTERNATIONAL RELATIONS"),
               ("society-and-culture", "SOCIETY & CULTURE"), ("science-and-technology", "SCIENCE & TECHNOLOGY"),
               ("art-and-literature", "ART & LITERATURE"), ("business-and-economics", "BUSINESS & ECONOMICS"))

    category = models.CharField(max_length=50, blank=False, null=False, choices=CATEGORIES)
    reports = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, through='Report', through_fields=('post', 'reporter'), related_name='reports')

    def num_likes(self):
        return self.liked.all().count()

    def num_dislikes(self):
        return self.disliked.all().count()

    def total_comments(self):
        total = 0
        total += self.comments.count()
        for comment in self.comments.all():
            total += comment.replies.count()
        
        return total

    def __str__(self):
        return self.title


PREFERENCES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    value = models.CharField(choices=PREFERENCES, default='Like', max_length=10)
    date_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)


class Dislike(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    value = models.CharField(choices=PREFERENCES, default='Like', max_length=10)
    date_disliked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_body = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, editable=False)
    new = models.BooleanField(default=True, editable=False)
    # reports = models.IntegerField(default=0)


    class Meta:
        ordering = ['created_on', 'commenter']

    def __str__(self):
        return '{} by {}'.format(self.comment_body, self.commenter)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    replier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, editable=False)
    new = models.BooleanField(default=True, editable=False)
    # reports = models.IntegerField(default=0)

    class Meta:
        ordering = ['created_on', 'replier']
        verbose_name_plural = 'replies'

    def __str__(self):
        return '{} by {}'.format(self.body, self.replier)


class Report(models.Model):
    TITLES = (('racism', "Racism"), ("nudity", "Nudity"))
    title = models.CharField(max_length=50, blank=False, null=False, choices=TITLES)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, default=None, blank=False, null=False, related_name='post_reports')
    # reply = models.ForeignKey(Reply, on_delete=models.CASCADE, default=None, blank=False, null=False, related_name='reply_reports')
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reporter', blank=False, null=False)
    # custom_title = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    new = models.BooleanField(default=True, editable=False)
    reviewed = models.BooleanField(default=False, editable=False)
    good = models.BooleanField(default=True, editable=False)
    bad = models.BooleanField(default=False, editable=False)


    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return '{} by {}'.format(self.title, self.reporter)


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.category:
        instance.category = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
