from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from refine.models import RefineIssues
from .forms import ReflectIssuesForm, ReflectContentsForm, ReflectProblemForm  # フォーム
from .models import ReflectIssues, ReflectContents, ReflectProblem
# Create your views here.

# これはテスト用


def test(request):
    return HttpResponse("これは統括的分析(再試行)")

# 統括的分析_論点の表示、論点とコメントの表示機能


class ReflectIssuesList(generic.ListView):
    model = ReflectIssues
    context_object_name = "Issues"
    template_name = "reflect/list.html"

    # ユーザごとにフィルターをかける
    def get_queryset(self):
        return ReflectIssues.objects.filter(create_user=self.request.user)

    # ListViewで複数モデルを取り込む
    def get_context_data(self, **kwargs):
        context = super(ReflectIssuesList, self).get_context_data(**kwargs)
        context.update({
            'reflect_contents_list': ReflectContents.objects.filter(create_user=self.request.user),
            'problem_contents_list': ReflectProblem.objects.filter(create_user=self.request.user),
        })
        return context


"""
    # 論点とコメントの表示機能
    def get_context_data(self, *args, **kwargs):
        reflectcontext = super().get_context_data(*args, **kwargs)
        reflectcontext['reflect_contents_list'] = ReflectContents.objects.all
        return reflectcontext

    # 振り返り問題点の表示機能
    def get_context_data(self, *args, **kwargs):
        problemcontext = super().get_context_data(*args, **kwargs)
        problemcontext['problem_contents_list'] = ReflectProblem.objects.all
        return (problemcontext)
"""


# 論点(のみ)の新規作成


class ReflectIssuesCreate(generic.CreateView):
    model = ReflectIssues
    form_class = ReflectIssuesForm
    template_name = "reflect/form.html"
    success_url = reverse_lazy("reflect:list")

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("reflect:list")
        return HttpResponseRedirect(success_url)

# 論点(のみ)の編集


class ReflectIssuesUpdate(generic.UpdateView):
    model = ReflectIssues
    form_class = ReflectIssuesForm
    template_name = "reflect/form.html"
    success_url = reverse_lazy("reflect:list")

# 論点(のみ)の削除


class ReflectIssuesDelete(generic.DeleteView):
    model = ReflectIssues
    context_object_name = "reflect"
    template_name = "reflect/delete.html"
    success_url = reverse_lazy("reflect:list")


# コメントの追加

class ReflectContentsCreate(generic.CreateView):
    model = ReflectContents
    form_class = ReflectContentsForm
    template_name = "reflect/c_form.html"

    # 参照論点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_issues'].queryset = ReflectIssues.objects.filter(create_user=self.request.user)
        return context

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("reflect:list")
        return HttpResponseRedirect(success_url)

# コメントを編集する機能


class ReflectContentsUpdate(generic.UpdateView):
    model = ReflectContents
    form_class = ReflectContentsForm
    template_name = "reflect/c_form.html"
    success_url = reverse_lazy("reflect:list")

    # 参照論点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_issues'].queryset = ReflectIssues.objects.filter(create_user=self.request.user)
        return context

# 削除機能


class ReflectContentsDelete(generic.DeleteView):
    model = ReflectContents
    context_object_name = "Issues"
    template_name = "reflect/c_delete.html"
    success_url = reverse_lazy("reflect:list")


# 問題点を追加する処理

class ProblemCreate(generic.CreateView):
    model = ReflectProblem
    form_class = ReflectProblemForm
    template_name = "reflect/p_form.html"

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("reflect:list")
        return HttpResponseRedirect(success_url)

# 問題点を削除する処理


class ProblemDelete(generic.DeleteView):
    model = ReflectProblem
    context_object_name = "problem"
    template_name = "reflect/p_delete.html"
    success_url = reverse_lazy("reflect:list")


# 問題点を編集する処理
class ProblemUpdate(generic.UpdateView):
    model = ReflectProblem
    form_class = ReflectProblemForm
    template_name = "reflect/p_form.html"
    success_url = reverse_lazy("reflect:list")
