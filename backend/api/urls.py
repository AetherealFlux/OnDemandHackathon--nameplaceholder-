from django.urls import path

from .views import *

urlpatterns = [
    path("addTodo", TodoView.addView, name="addTodo"),
]