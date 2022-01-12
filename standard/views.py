from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Standard
from .forms import StandardForm  # フォーム
# Create your views here.


# 評価基準の表示機能


class StandardList(generic.ListView):
    model = Standard
    context_object_name = "standards"
    template_name = "standard/list.html"

    # ユーザごとにフィルターをかける
    def get_queryset(self):
        return Standard.objects.filter(create_user=self.request.user)

# 評価基準の作成機能


class StandardCreate(generic.CreateView):
    model = Standard
    form_class = StandardForm
    template_name = "standard/form.html"

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("standard:list")
        return HttpResponseRedirect(success_url)

# 編集


class StandardUpdate(generic.UpdateView):
    model = Standard
    orm_class = StandardForm
    template_name = "standard/form.html"
    success_url = reverse_lazy("standard:list")

# 削除機能


class StandardDelete(generic.DeleteView):
    model = Standard
    context_object_name = "standard"
    template_name = "standard/delete.html"
    success_url = reverse_lazy("standard:list")
