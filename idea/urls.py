from django.urls import path
# この下にviews.pyで作ったものを記載して読み込ませる
from . import views  # views用のimport

app_name = "idea"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    path('', views.Home, name="home"),  # ホーム画面
    path("list/", views.IdeaList.as_view(), name="list"),  # アイディア一覧
    path("detail/<int:pk>", views.IdeaDetail.as_view(), name="detail"),  # 詳細
    path("create/", views.IdeaCreate.as_view(), name="create"),  # 新規投稿
    path("update/<int:pk>", views.IdeaUpdate.as_view(), name="update"),  # 編集
    path("delete/<int:pk>", views.IdeaDelete.as_view(), name="delete"),  # 削除
    path("v_list", views.VoteList.as_view(), name="v_list"),  # 投票一覧
    path("v_detail/<int:pk>", views.VoteDetail.as_view(), name="v_detail"),  # 投票画面遷移
    # ここからは投票機能
    path('index', views.index, name="index"),  # 接続テスト用
    path("vote_update/<int:pk>", views.VoteUpdate.as_view(), name="vote_update"),  # 編集
    path('Vote/<int:pk>/', views.Vote, name='Vote'),  # 投票を増やす機能
    path('Vote_decrease/<int:pk>/', views.Vote_decrease, name='Vote_decrease'),  # 投票を減らす機能(best)
    path('Vote_decrease2/<int:pk>/', views.Vote_decrease2, name='Vote_decrease2'),  # 投票を減らす機能(better)

]
