from django import forms
from .models import Idea

# class IdeaCreateで使う


class IdeaForm(forms.ModelForm):
    class Meta:
        # どのモデルをフォームにするか指定
        model = Idea
        # そのフォームの中から表示するフィールドを指定
        fields = ('title', 'description', 'cycle_num')
        # ラベルを設定
        labels = {'title': 'アイディア',
                  'description': '説明',
                  'cycle_num': 'サイクル回数'}

    """
        # フォームを綺麗にするための記載(よくわからない)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    """
