from django.db import models  # 最初はこれだけ
from django.contrib.auth import get_user_model  # ユーザー情報取得

# Create your models here.
# アイディア一覧


class Idea(models.Model):
    title = models.TextField("アイディア", blank=False)
    description = models.TextField("詳細", blank=True)
    cycle_num = models.IntegerField("サイクル回数", blank=False)
    best_choice = models.IntegerField(default=0)
    better_choice = models.IntegerField(default=0)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
