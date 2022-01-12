from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import RefineContents, RefineIssues
from .forms import RefineIssuesForm, CommentForm  # フォーム
# Create your views here.

# これはテスト用


def test(request):
    return HttpResponse("これは精緻化")


# これは統括的分析その1の画面
def Home(request):
    return render(request, "refine/home.html")


# 精緻化の一覧表示機能、前半で論点、優先順位を取得
# # 後半で論点、コメントタイプ、内容を取得


class RefineList(generic.ListView):
    model = RefineIssues
    context_object_name = "Issues"
    template_name = "refine/list.html"
    # ユーザごとにフィルターをかける

    def get_queryset(self):
        return RefineIssues.objects.filter(create_user=self.request.user)

# 精緻化のコメントなどを取得する関数
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contents_list'] = RefineContents.objects.filter(create_user=self.request.user)
        return context


"""
    # 精緻化のコメントなどを取得する関数
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contents_list'] = RefineContents.objects.all
        return context
"""
# 論点の作成機能


class RefineCreate(generic.CreateView):
    model = RefineIssues
    form_class = RefineIssuesForm
    # fields = ('issues', 'priority')
    template_name = "refine/form.html"

    # 優先度の初期値を0にする処理
    def get_initial(self):
        initial = super().get_initial()
        initial["priority"] = 0
        return initial

# フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("refine:list")
        return HttpResponseRedirect(success_url)


# 論点と優先順位の編集機能


class RefineUpdate(generic.UpdateView):
    model = RefineIssues
    form_class = RefineIssuesForm
    template_name = "refine/update.html"
    success_url = reverse_lazy("refine:list")

# 削除機能


class RefineDelete(generic.DeleteView):
    model = RefineIssues
    context_object_name = "Issues"
    template_name = "refine/delete.html"
    success_url = reverse_lazy("refine:list")


# ここからはコメントを入力するほう
# 精緻化のコメントを作成する機能

class CommentCreate(generic.CreateView):
    model = RefineContents
    form_class = CommentForm
    template_name = "refine/c_form.html"
    success_url = reverse_lazy("refine:list")

    # 参照論点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_idea'].queryset = RefineIssues.objects.filter(create_user=self.request.user)
        return context

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("refine:list")
        return HttpResponseRedirect(success_url)

# コメントを編集する機能


class CommentUpdate(generic.UpdateView):
    model = RefineContents
    fields = ('ref_issues', 'comment_type', 'comment_content')
    template_name = "refine/c_form.html"
    success_url = reverse_lazy("refine:list")

    # 参照論点を自分のものだけ表示するフィルター
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['ref_idea'].queryset = RefineIssues.objects.filter(create_user=self.request.user)
        return context

# 削除機能


class CommentDelete(generic.DeleteView):
    model = RefineContents
    context_object_name = "Issues"
    template_name = "refine/c_delete.html"
    success_url = reverse_lazy("refine:list")
