from django import forms

from .models import Post, Product

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'rating')


class SortForm(forms.ModelForm):
    maxResolution = forms.CharField(max_length=100)
    maxExcerpt = forms.IntegerField()
    price = forms.IntegerField()
    class Meta:
        model = Product
        fields = ('category',)