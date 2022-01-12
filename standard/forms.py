from django import forms
from .models import Standard

# class Standard...で使う


class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = ('standard',)
        labels = {'standard': '評価基準'}
