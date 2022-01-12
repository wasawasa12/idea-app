from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from standard.models import Standard
from .models import Matrix
from .forms import MatrixForm  # フォーム
from idea.models import Idea
# Create your views here.

# これはテスト用

"""
def test(request):
    return HttpResponse("this is matrix view!!")
"""

# マトリクスの一覧表示機能


class MatrixList(generic.ListView):
    model = Matrix
    context_object_name = "matrixes"
    template_name = "matrix/list.html"
    # ユーザごとにフィルターをかける

    def get_queryset(self):
        return Matrix.objects.filter(create_user=self.request.user)

# マトリクスの要素作成機能


class MatrixCreate(generic.CreateView):
    model = Matrix
    form_class = MatrixForm
    template_name = "matrix/form.html"

    # 参照アイディア、評価基準を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_idea'].queryset = Idea.objects.filter(create_user=self.request.user)
        context['form'].fields['ref_standard'].queryset = Standard.objects.filter(create_user=self.request.user)
        return context

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分(自動ユーザー登録)

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("matrix:list")
        return HttpResponseRedirect(success_url)

# マトリクス編集機能


class MatrixUpdate(generic.UpdateView):
    model = Matrix
    form_class = MatrixForm
    template_name = "matrix/form.html"
    success_url = reverse_lazy("matrix:list")

    # 参照アイディア、評価基準を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_idea'].queryset = Idea.objects.filter(create_user=self.request.user)
        context['form'].fields['ref_standard'].queryset = Standard.objects.filter(create_user=self.request.user)
        return context

# マトリクス削除機能


class MatrixDelete(generic.DeleteView):
    model = Matrix
    context_object_name = "matrixes"
    template_name = "matrix/delete.html"
    success_url = reverse_lazy("matrix:list")
