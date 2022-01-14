from django.shortcuts import render, get_object_or_404  # 後ろは追加
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect  # 追加
from django.urls import reverse_lazy, reverse
from .models import Idea
from django.template import loader
from .forms import IdeaForm  # フォーム
from django.db.models import F  # データベースを操作するF関数

# Create your views here.


def Home(request):
    template = loader.get_template('idea/home.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return render(request,"idea/home.html")
# アイディアの表示機能


class IdeaList(generic.ListView):
    model = Idea
    context_object_name = "idea"  # HTMLを表示するときに使う変数名(for文を使うのでわざとsをつける)
    template_name = "idea:idea_list.html"

    # ユーザごとにフィルターをかける
    def get_queryset(self):
        return Idea.objects.filter(create_user=self.request.user)

# アイディアの詳細表示機能


class IdeaDetail(generic.DetailView):
    model = Idea
    context_object_name = "opinion"  # HTMLを表示するときに使う変数名

# アイディアの投稿機能(こっちはforms.pyを使ってフィールド指定)


class IdeaCreate(generic.CreateView):
    model = Idea
    form_class = IdeaForm

    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user = self.request.user
        qryset.save()
        print(qryset)
        success_url = reverse("idea:list")
        return HttpResponseRedirect(success_url)

    # 初期値の設定,サイクル回数=1,best,betterを0設定

    def get_initial(self):
        initial = super().get_initial()
        initial["cycle_num"] = 1
        initial["best_choice"] = 0
        initial["better_choice"] = 0
        return initial

# アイディアの編集機能(こっちはfieldsで指定している)


class IdeaUpdate(generic.UpdateView):
    model = Idea
    fields = ('title', 'description', 'cycle_num')
    success_url = reverse_lazy("idea:list")  # 登録が終わるとトップページに戻る

# アイディアの削除機能


class IdeaDelete(generic.DeleteView):
    model = Idea
    context_object_name = "opinion"
    success_url = reverse_lazy("idea:list")


# 投票機能(新)
# 投票の一覧画面
class VoteList(generic.ListView):
    model = Idea
    context_object_name = "idea"
    template_name = 'idea/v_list.html'

    # ユーザごとにフィルターをかける
    def get_queryset(self):
        return Idea.objects.filter(create_user=self.request.user)


# 投票機能
class VoteUpdate(generic.UpdateView):
    model = Idea
    fields = ('best_choice', 'better_choice', )
    template_name = 'idea/v_form.html'
    success_url = reverse_lazy("idea:v_list")  # 登録が終わるとトップページに戻る

# 投票内容を一つ減らす機能


def Vote_decrease(request, pk):
    """指定されたpkのIdeaのbestを1減らして、一覧表示ページにリダイレクトする"""
    var = Idea.objects.get(pk=pk)
    if var.best_choice != 0:
        # F関数使用
        Idea.objects.filter(pk=pk).update(best_choice=F('best_choice') - 1)

    success_url = reverse("idea:v_list")
    return HttpResponseRedirect(success_url)


def Vote_decrease2(request, pk):
    """指定されたpkのIdeaのbestを1減らして、一覧表示ページにリダイレクトする"""
    var = Idea.objects.get(pk=pk)
    if var.better_choice != 0:
        # F関数使用
        Idea.objects.filter(pk=pk).update(better_choice=F('better_choice') - 1)

    success_url = reverse("idea:v_list")
    return HttpResponseRedirect(success_url)

# 投票する画面


class VoteDetail(generic.DetailView):
    model = Idea
    context_object_name = "idea"
    template_name = 'idea/v_detail.html'

# 入力された結果を反映させる


def Vote(request, pk):
    # ここで評価を受け取る
    content = request.POST.get("choice")
    # ラジオでbestが選択された場合best_choiceをプラス1
    if content == "best":
        Idea.objects.filter(pk=pk).update(best_choice=F('best_choice')+1)
    # betterが選択された場合better_choiceをプラス1
    elif content == "better":
        Idea.objects.filter(pk=pk).update(better_choice=F('better_choice')+1)

    success_url = reverse_lazy("idea:v_list")
    return HttpResponseRedirect(success_url)

# これはテスト用


def index(request):
    return HttpResponse("Hello World")
