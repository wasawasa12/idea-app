from django.db import models
from reflect.models import ReflectProblem
from django.contrib.auth import get_user_model  # ユーザー情報取得
# Create your models here.


class Retry(models.Model):
    ref_problem = models.ForeignKey('reflect.ReflectProblem', on_delete=models.CASCADE)
    content = models.TextField()
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
