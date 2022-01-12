from django.urls import path
from . import views

app_name = "reflect"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    path("test/", views.test, name="test"),
    path("", views.ReflectIssuesList.as_view(), name="list"),
    path("create/", views.ReflectIssuesCreate.as_view(), name="create"),
    path("update/<int:pk>", views.ReflectIssuesUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.ReflectIssuesDelete.as_view(), name="delete"),
    path("c_create", views.ReflectContentsCreate.as_view(), name="c_create"),
    path("c_update/<int:pk>", views.ReflectContentsUpdate.as_view(), name="c_update"),
    path("c_delete/<int:pk>", views.ReflectContentsDelete.as_view(), name="c_delete"),
    path("p_create", views.ProblemCreate.as_view(), name="p_create"),
    path("p_delete/<int:pk>", views.ProblemDelete.as_view(), name="p_delete"),
    path("p_update/<int:pk>", views.ProblemUpdate.as_view(), name="p_update"),
]
