from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={
            "class": "form-control form-body",
            "placeholder": "Leave a comment!"
        })
    )

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')