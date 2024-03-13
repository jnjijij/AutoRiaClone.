from django import forms

from .models import Comment
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['field1', 'field2', ...]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['field1', 'field2', ...]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
