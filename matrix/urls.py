from django.urls import path
from . import views

app_name = "matrix"
urlpatterns = [
    # path("ここはurl", ここはviewsのどのメソッドか, {% url %}で使う時の名前)
    #path("", views.test, name="test"),
    path("", views.MatrixList.as_view(), name="list"),
    path("create/", views.MatrixCreate.as_view(), name="create"),
    path("update/<int:pk>", views.MatrixUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.MatrixDelete.as_view(), name="delete"),

]
