from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author","body")
        widgets = {
            # "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"This is Title PlaceHolder"}),
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class":"form-control", "value":"", "id":"user", "type":"hidden"}),
            # "author": forms.Select(attrs={"class":"form-control", value: user.id}),
            "body": forms.Textarea(attrs={"class":"form-control"})
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            # "author": forms.Select(attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"})
        }