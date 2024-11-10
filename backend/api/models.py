from django.db import models
from django import forms

class Todo(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=True)
    estimatedDuration = models.CharField(max_length=128, blank=True)
    duration = models.CharField(max_length=128, blank=True)
    completed = models.BooleanField(default=False)
    feedback = models.TextField(null=True)

class SubTodo(models.Model):
    todo = models.ForeignKey(to="Todo", on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    estimatedDuration = models.CharField(max_length=128, blank=True)
    duration = models.IntegerField(null=True)
    completed = models.BooleanField(default=False)


class Habit(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True)
    plan = models.TextField(blank=True)

class Schedule(models.Model):
    content = models.TextField(blank=False)
    date = models.DateField(auto_now=True)
    feedback = models.TextField(blank=True)

class TodoSummary(models.Model):
    content = models.TextField(blank=False)
    date = models.DateField()

class HabitSummary(models.Model):
    content = models.TextField(blank=False)
    date = models.DateField()
