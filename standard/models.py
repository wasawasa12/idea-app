from django.db import models
from django.contrib.auth import get_user_model  # ユーザー情報取得

# Create your models here.

# 評価基準
"""
モデルを作成したら
python manage.py makemigrations standard(アプリ名)
python manage.py migrate standard
を実行してモデルを登録
"""


class Standard(models.Model):
    standard = models.CharField(max_length=50)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.standard
