from django.urls import path
from . import views

app_name = "retry"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    path("", views.RetryList.as_view(), name="list"),
    path("create/", views.RetryCreate.as_view(), name="create"),
    path("update/<int:pk>", views.RetryUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.RetryDelete.as_view(), name="delete"),
]
