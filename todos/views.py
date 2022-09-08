from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todos.models import TodoList
from todos.models import TodoItem
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.urls import reverse


# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos.html"

    def get_queryset(self):
        return TodoList.objects.all()


class TodoListDetail(DetailView):
    model = TodoList
    template_name = "detail.html"

    # def get_queryset(self):
    #     return TodoList.objects.all()


class TodoListCreate(CreateView):
    model = TodoList
    template_name = "new.html"
    fields = ["name"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListUpdate(UpdateView):
    model = TodoList
    template_name = "new.html"
    fields = ["name"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListDelete(DeleteView):
    model = TodoList
    template_name = "delete.html"
    success_url = reverse_lazy("todo_list_list")


class TodoItemCreate(CreateView):
    model = TodoItem
    template_name = "create_item.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse("todo_list_detail", args=[self.object.list.id])

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(TodoItemCreate, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class TodoItemUpdate(UpdateView):
    model = TodoItem
    template_name = "edit_item.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse("todo_list_detail", args=[self.object.list.id])
