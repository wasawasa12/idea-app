from django import forms
from .models import RefineIssues, RefineContents

# class RefineIssues...で使う


class RefineIssuesForm(forms.ModelForm):
    class Meta:
        model = RefineIssues
        fields = ('issues', 'priority')
        labels = {'issues': '論点',
                  'priority': '優先度'}

# class CommentCreate,Updateで使う


class CommentForm(forms.ModelForm):
    class Meta:
        model = RefineContents
        fields = ('ref_issues', 'comment_type', 'comment_content')
        labels = {'ref_issues': '参照論点',
                  'comment_type': 'コメントタイプ', 'comment_content': 'コメント内容'}
