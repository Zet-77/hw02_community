from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        labels = {
             'text': 'Текс поста',
             'group': 'Гуппа к которой будет относится ваш пост' 
        }

    