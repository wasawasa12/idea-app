from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Retry
from reflect.models import ReflectProblem
from .forms import RetryForm  # フォーム
# Create your views here.

# 一覧表示


class RetryList(generic.ListView):
    model = Retry
    context_object_name = "contents"
    template_name = "retry/list.html"

    # ユーザごとにフィルターをかける
    def get_queryset(self):
        return Retry.objects.filter(create_user=self.request.user)

# 新規作成


class RetryCreate(generic.CreateView):
    model = Retry
    form_class = RetryForm
    template_name = "retry/form.html"
    success_url = reverse_lazy("retry:list")

    # 参照問題点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_problem'].queryset = ReflectProblem.objects.filter(create_user=self.request.user)
        return context

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("retry:list")
        return HttpResponseRedirect(success_url)


# 編集機能


class RetryUpdate(generic.UpdateView):
    model = Retry
    form_class = RetryForm
    template_name = "retry/form.html"
    success_url = reverse_lazy("retry:list")

    # 参照問題点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_problem'].queryset = ReflectProblem.objects.filter(create_user=self.request.user)
        return context

# 削除機能


class RetryDelete(generic.DeleteView):
    model = Retry
    context_object_name = "content"
    template_name = "retry/delete.html"
    success_url = reverse_lazy("retry:list")
