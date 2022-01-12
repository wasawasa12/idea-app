from django.db import models
from django.contrib.auth import get_user_model  # ユーザー情報取得

# Create your models here.

# comment_typeの選択肢を設定
TYPE = [('Positive', 'ポジティブ'), ('Negative', 'ネガティブ'), ('Conclusion', '結論'), ('correspondence', '対応')]


class RefineIssues(models.Model):
    issues = models.TextField(blank=False)
    priority = models.IntegerField()
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.issues


class RefineContents(models.Model):
    ref_issues = models.ForeignKey('RefineIssues', on_delete=models.CASCADE)
    comment_type = models.CharField(max_length=20, choices=TYPE)
    comment_content = models.TextField(blank=False)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
