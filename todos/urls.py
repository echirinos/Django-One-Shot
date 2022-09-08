from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetail,
    TodoListCreate,
    TodoListUpdate,
    TodoListDelete,
    TodoItemCreate,
    TodoItemUpdate,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoListDetail.as_view(), name="todo_list_detail"),
    path("create/", TodoListCreate.as_view(), name="todo_list_create"),
    path("<int:pk>/edit/", TodoListUpdate.as_view(), name="todo_list_update"),
    path("<int:pk>/delete/", TodoListDelete.as_view(), name="todo_list_delete"),
    path("items/create/", TodoItemCreate.as_view(), name="todo_item_create"),
    path(
        "items/<int:pk>/edit/",
        TodoItemUpdate.as_view(),
        name="todo_item_update",
    ),
]
