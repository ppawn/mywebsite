from django import forms
from .models import Comment,Visit_Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']

class Visit_CommentForm(forms.ModelForm):
    class Meta:
        model = Visit_Comment
        fields = ['name', 'text']
