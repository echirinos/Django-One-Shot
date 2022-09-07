from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todos.models import TodoList


# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos.html"

    def get_queryset(self):
        return TodoList.objects.all()
