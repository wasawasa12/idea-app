from django import forms
from .models import ReflectIssues, ReflectContents, ReflectProblem

# class ReflectIssues...で使う


class ReflectIssuesForm(forms.ModelForm):
    class Meta:
        model = ReflectIssues
        fields = ('issues',)
        labels = {'issues': '論点'}


class ReflectContentsForm(forms.ModelForm):
    class Meta:
        model = ReflectContents
        fields = ('ref_issues', 'comment_type', 'comment_content')
        labels = {'ref_issues': '参照論点', 'comment_type': 'コメントタイプ', 'comment_content': 'コメント内容'}


class ReflectProblemForm(forms.ModelForm):
    class Meta:
        model = ReflectProblem
        fields = ('problem',)
        labels = {'problem': '問題点'}
