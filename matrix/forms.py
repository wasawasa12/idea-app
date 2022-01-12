from django import forms
from .models import Matrix

# class MatrixCreateで使う


class MatrixForm(forms.ModelForm):
    class Meta:
        model = Matrix
        fields = ('ref_idea', 'ref_standard', 'comment_type', 'comment_content')
        labels = {'ref_idea': '対象アイディア',
                  'ref_standard': '対象評価基準',
                  'comment_type': 'コメントの種類',
                  'comment_content': 'コメント内容'}
