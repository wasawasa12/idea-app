from django.shortcuts import render
from .forms import LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm, User  # Formのインポート
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView  # ログイン関連のビューはdjangoで用意されている
from django.contrib.auth import get_user_model  # ユーザー情報取得
from django.contrib.auth.mixins import UserPassesTestMixin  # 他人のマイページは開けないようにする
from django.views import generic
from django.shortcuts import redirect, resolve_url  # 追加
from django.urls import reverse_lazy  # 追加　遅延評価用
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # 退会処理
# Create your views here.

'''トップページ'''


class TopView(generic.TemplateView):
    template_name = 'account/top.html'

# ログイン


class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

# ログアウト


class Logout(LogoutView):
    template_name = 'account/logout_done.html'


# 自分しかアクセスできないようにするMixin(My Pageのため)


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']


'''マイページ'''


class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'account/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される


'''サインアップ'''


class Signup(generic.CreateView):
    template_name = 'account/user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()  # formの情報を保存
        return redirect('account:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''


class SignupDone(generic.TemplateView):
    template_name = 'account/signup_done.html'


'''ユーザー登録情報の更新'''


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'account/user_form.html'

    def get_success_url(self):
        return resolve_url('account:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context


'''パスワード変更'''


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('account:password_change_done')
    template_name = 'account/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


'''パスワード変更完了'''


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


# 退会処理(ここは退会画面にアクセスを行う制限)
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.username == self.kwargs['username'] or user.is_superuser

# 退会処理


class UserDeleteView(OnlyYouMixin, generic.DeleteView):
    template_name = "account/delete.html"
    success_url = reverse_lazy("account:top")
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
