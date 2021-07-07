from django import forms
from django.forms.widgets import Widget
from .models import Post

class NewPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50,'style':'resize:none;','placeholder':'Type new post here' }), label='')

    class Meta:
        model = Post
        fields = ['content']
