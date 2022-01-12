from django.db import models
from idea.models import Idea
from standard.models import Standard
from django.contrib.auth import get_user_model  # ユーザー情報取得

# Create your models here.

# comment_typeの選択肢を設定
TYPE = [('Positive', 'ポジティブ'), ('Negative', 'ネガティブ'), ('Addion', '追加コメント'), ('other', 'その他')]


class Matrix(models.Model):
    ref_idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE)
    ref_standard = models.ForeignKey('standard.Standard', on_delete=models.CASCADE)
    comment_type = models.CharField(max_length=20, choices=TYPE)
    comment_content = models.TextField(blank=True)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
