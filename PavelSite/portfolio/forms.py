from django import forms
from django.core.exceptions import ValidationError

from .models import *


# class AddPostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Post
#         fields = ['title', 'slug', 'content', 'photo', 'is_published']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-input'}),
#             'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
#         }
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) > 200:
#             raise ValidationError('Длина превышает 200 символов')
#
#         return title
