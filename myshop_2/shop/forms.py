from django import forms

from .models import Post, Product

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'rating')


CHOICES = (
    (0, 'a'),
    (1, 'b'),
    (2, 'c'),
)

class SortForm(forms.Form):
    letters = forms.MultipleChoiceField(
            choices=CHOICES, 
            label="", 
            required=False) 


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class UserForm(forms.Form):
    name = forms.CharField(label="name")
    age = forms.IntegerField(label="age")


class listClass(forms.Form):
    listC = ("Sony", "Canon", "Nikon", "Olympus", "Fujifilm")

    listRes = ("6000x4000", "5472x3648", "5184x3456", "4608x3456", "4592x3448", "3840x2160")