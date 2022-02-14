from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author", "category", "body", "pics")
        widgets = {
            # "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"This is Title PlaceHolder"}),
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class":"form-control", "value":"", "id":"user", "type":"hidden"}),
            "category": forms.Select(choices=choice_list, attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),
            "pics": forms.TextInput(attrs={"class":"form-control", "placeholder":"Post picture url should be add"}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "pics")
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class":"form-control"}),
            # "author": forms.Select(attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),
            "pics": forms.TextInput(attrs={"class":"form-control" , "placeholder":"Post picture url should be add"}),
        }