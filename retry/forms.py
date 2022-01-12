from django import forms
from .models import Retry

# class Retry...で使う


class RetryForm(forms.ModelForm):
    class Meta:
        model = Retry
        fields = ('ref_problem', 'content')
        labels = {'ref_problem': '参照問題点',
                  'content': '再試行の内容'}
