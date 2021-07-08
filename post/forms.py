from django import forms
from .models import Post

class DocumentForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('store_name', 'where', 'food_category', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'description')



  


    