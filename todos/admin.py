from django.contrib import admin

from todos.models import TodoList

from todos.models import TodoItem


class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)


class TodoItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoItem, TodoItemAdmin)


# Register your models here.
