from api import models
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpRequest
from django.db.models import Model
from django import forms

def addTodo(request: HttpRequest) -> HttpResponse:
    class Form(forms.ModelForm):
        class Meta:
            model = models.Todo
            fields = "__all__"
    form = Form(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        models.Todo.objects.create(**data)
    else:
        return HttpResponseBadRequest()
    return HttpResponse()

def addHabit(request: HttpRequest) -> HttpResponse:
    class Form(forms.ModelForm):
        class Meta:
            model = models.Habit
            fields = "__all__"
    form = Form(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        models.Habit.objects.create(**data)
    else:
        return HttpResponseBadRequest()
    return HttpResponse()

def getTodos(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"todos": models.Todo.objects.all().values_list()})

def getHabits(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"Habits": models.Habit.objects.all().values_list()})

def genSubtodos(request: HttpRequest) -> HttpResponse:
    ...

def genHabitTodo(request: HttpRequest) -> HttpResponse:
    ...

def genSchedule(request: HttpRequest) -> HttpResponse:
    ...

def genSummary(request: HttpRequest) -> HttpResponse:
    ...
