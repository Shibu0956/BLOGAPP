from django import forms
from Blogapp.models import Myblog


class Blogform(forms.ModelForm):
    class Meta:
        model = Myblog
        fields = "__all__"