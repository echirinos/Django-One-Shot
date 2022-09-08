from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todos.models import TodoList
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos.html"

    def get_queryset(self):
        return TodoList.objects.all()


class TodoListDetail(DetailView):
    model = TodoList
    template_name = "detail.html/"

    # def get_queryset(self):
    #     return TodoList.objects.all()


class TodoListCreate(CreateView):
    model = TodoList
    template_name = "new.html"
    fields = ["name"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoListUpdate(UpdateView):
    model = TodoList
    template_name = "new.html"
    fields = ["name"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
