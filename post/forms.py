from django import forms
# from django.db.models import fields
from .models import Post

class DocumentForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('store_name', 'where', 'food_category', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'description')

  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.fields['where'].widget.attrs['class'] = 'form-control'
  #   self.fields['where'].widget.attrs['id'] = 'where'
  #   self.fields['where'].widget.attrs['name'] = 'where'
  #   self.fields['where'].widget.attrs['placeholder'] = 'ご飯屋を入力'

  


    