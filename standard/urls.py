from django.urls import path
from . import views

app_name = "standard"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    path("", views.StandardList.as_view(), name="list"),
    path("create/", views.StandardCreate.as_view(), name="create"),
    #path("detail/<int:pk>", views.StandardDetail.as_view(), name="detail"),
    path("update/<int:pk>", views.StandardUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.StandardDelete.as_view(), name="delete"),

]
