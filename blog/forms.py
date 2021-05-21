from django import forms

from tinymce.widgets import TinyMCE

from blog.models import BlogPost, Comment, Reply


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class CreateBlogPostForm(forms.ModelForm):
    AUTHORS = (("1", "HISTORY"), ("2", "POLITICS & INTERNATIONAL RELATIONS"), ("3", "SOCIETY & CULTURE"),
               ("4", "SCIENCE & TECHNOLOGY"), ("5", "ART & LITERATURE"), ("6", "BUSINESS & ECONOMICS"))

    category = forms.ChoiceField(choices=AUTHORS)

    class Meta:
        model = BlogPost
        fields = ['category', 'title', 'body', 'image']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category', 'title', 'body', 'image']

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.category = self.cleaned_data['category']
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Comment
        fields = ('body',)


class ReplyForm(forms.ModelForm):
    body = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Reply
        fields = ('body',)
