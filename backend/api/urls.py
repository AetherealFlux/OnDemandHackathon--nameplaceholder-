from django.urls import path

from .views import *

urlpatterns = [
    path("addTodo", addTodo, name="addTodo"),
    path("addHabit", addHabit, name="addHabit"),
    path("getTodos", getTodos, name="getTodos"),
    path("getHabits", getHabits, name="getHabits"),
    path("genSchedule", genSchedule, name="genSchedule"),
    path("genSummary", genSummary, name="genSummary"),
    path("genSubtodos", genSubtodos, name="genSubtodos"),
    path("genHabitPlan", genHabitPlan, name="genHabitPlan"),
    path("genHabitTodo", genHabitTodo, name="genHabitTodo"),
]