from django.urls import path

from .views import *

urlpatterns = [
    path("addTodo", addTodo, name="addTodo"),
    path("addHabit", addHabit, name="addHabit"),
    path("getTodos", getTodos, name="getTodos"),
    path("getHabits", getHabits, name="getHabits")
]