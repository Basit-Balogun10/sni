from django import forms

from tinymce.widgets import TinyMCE

from blog.models import BlogPost, Comment, Reply, PostReport


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class CreateBlogPostForm(forms.ModelForm):
    CATEGORIES = (("1", "HISTORY"), ("2", "POLITICS & INTERNATIONAL RELATIONS"), ("3", "SOCIETY & CULTURE"),
               ("4", "SCIENCE & TECHNOLOGY"), ("5", "ART & LITERATURE"), ("6", "BUSINESS & ECONOMICS"))

    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = BlogPost
        fields = ['category', 'title', 'body', 'image', 'author_img']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category', 'title', 'body', 'image', 'author_img']

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.category = self.cleaned_data['category']
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
        
        if self.cleaned_data['author_img']:
            blog_post.image = self.cleaned_data['author_img']

        if commit:
            blog_post.save()
        return blog_post


class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 50, 'rows': 60}
        )
    )

    class Meta:
        model = Comment
        fields = ('comment_body',)


class ReplyForm(forms.ModelForm):
    body = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 50, 'rows': 60}
        )
    )

    class Meta:
        model = Reply
        fields = ('body',)
