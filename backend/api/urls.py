from django.urls import path

from .views import *

urlpatterns = [
    path("addTodo", Todos.addView, name="addTodo"),
    path("editTodo", Todos.editView, name="editTodo"),
    path("deleteTodo", Todos.deleteView, name="deleteTodo"),
    path("toggleTodo", )
]