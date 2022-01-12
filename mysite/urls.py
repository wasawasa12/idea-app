"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # includeは追加


urlpatterns = [
    path('', include('account.urls')),  # 認証機能パス
    path('admin/', admin.site.urls),
    path('idea/', include('idea.urls')),  # 追加、指定されたもの以外のアクセスはidea.urlsを参照する
    path('standard/', include('standard.urls')),  # パスの追加
    path('matrix/', include('matrix.urls')),  # パスの追加
    path('refine/', include('refine.urls')),  # パスの追加
    path('reflect/', include('reflect.urls')),  # 統括的分析(振り返り)パスの追加
    path('retry/', include('retry.urls')),  # 再試行の設計
]
