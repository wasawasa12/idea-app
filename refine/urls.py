from django.urls import path
from . import views

app_name = "refine"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    path("test", views.test, name="test"),
    path("home", views.Home, name="home"),
    path("", views.RefineList.as_view(), name="list"),
    path("create", views.RefineCreate.as_view(), name="create"),
    path("update/<int:pk>", views.RefineUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.RefineDelete.as_view(), name="delete"),
    path("c_create", views.CommentCreate.as_view(), name="c_create"),
    path("c_update/<int:pk>", views.CommentUpdate.as_view(), name="c_update"),
    path("c_delete/<int:pk>", views.CommentDelete.as_view(), name="c_delete"),
]
