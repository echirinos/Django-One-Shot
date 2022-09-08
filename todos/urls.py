from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetail,
    TodoListCreate,
    TodoListUpdate,
    TodoListDelete,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoListDetail.as_view(), name="todo_list_detail"),
    path("create/", TodoListCreate.as_view(), name="todo_list_create"),
    path("<int:pk>/edit/", TodoListUpdate.as_view(), name="todo_list_update"),
    path("<int:pk>/delete/", TodoListDelete.as_view(), name="todo_list_delete"),
]
