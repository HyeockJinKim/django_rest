from django import forms
from .models import Rest


class RestForm(forms.ModelForm):
    class Meta:
        model = Rest
        fields = ('title', 'keyword',)
