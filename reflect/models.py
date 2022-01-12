from django.db import models
from django.contrib.auth import get_user_model  # ユーザー情報取得
# Create your models here.


class ReflectIssues(models.Model):
    issues = models.CharField(max_length=50)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.issues


# comment_typeの選択肢を設定
TYPE = [('Positive', 'ポジティブ'), ('Negative', 'ネガティブ'), ('Conclusion', '結論')]


class ReflectContents(models.Model):
    ref_issues = models.ForeignKey('ReflectIssues', on_delete=models.CASCADE)
    comment_type = models.CharField(max_length=20, choices=TYPE)
    comment_content = models.TextField(blank=False)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class ReflectProblem(models.Model):
    problem = models.TextField(blank=False)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.problem
