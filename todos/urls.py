from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetail,
    TodoListCreate,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoListDetail.as_view(), name="todo_list_detail"),
    path("create/", TodoListCreate.as_view(), name="todo_list_create"),
]
