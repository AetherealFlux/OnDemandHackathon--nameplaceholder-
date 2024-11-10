from api import models
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpRequest
from django.db.models import Model
from django import forms
from api import ai
import json

def addTodo(request: HttpRequest) -> HttpResponse:
    class Form(forms.ModelForm):
        class Meta:
            model = models.Todo
            fields = "__all__"
    form = Form(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        todo = models.Todo.objects.create(**data)
        if (request.GET.get("subtasks")):
            subtasks = json.load(request.GET["subtasks"])
            for subtask in subtasks:
                models.SubTodo.objects.create(todo=todo, title=subtask["title"], estimatedDuration=subtask["estimatedDuration"])
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

def getTodoList() -> list[dict]:
    todos = list(models.Todo.objects.values())
    for todo in todos:
        pk = todo["id"]
        subTodos = models.SubTodo.objects.filter(todo=pk)
        if subTodos.exists():
            todo["subTodo"] = list(subTodos.values())
    return todos

def getTodos(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"todos": getTodoList()})

def getHabits(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"Habits": list(models.Habit.objects.values())})

def genSubtodos(request: HttpRequest) -> HttpResponse:
    if request.GET.get("todo"):
        return JsonResponse({"data": ai.Gen.genSubtodos(request.GET["todo"])})
    else:
        return HttpResponseBadRequest()

def genHabitPlan(request: HttpRequest) -> HttpResponse:
    if request.GET.get("habit"):
        return JsonResponse({"data": ai.Gen.genHabitPlan(request.GET["habit"])})
    else:
        return HttpResponseBadRequest()

def genHabitTodo(request: HttpRequest) -> HttpResponse:
    if request.GET.get("habit") and request.GET.get("plan"):
        return JsonResponse({"data": ai.Gen.genHabitTodo(request.GET["habit"], request.GET["plan"])})
    else:
        return HttpResponseBadRequest()

def genSchedule(request: HttpRequest) -> HttpResponse:
    if request.GET.get("comment"):
        todos = getTodoList()
        schedule = ai.Gen.genSchedule(data=str({"comment": request.GET["commnet"], "tasks": str(todos)}))
        models.Schedule.objects.create(content=schedule)
        return JsonResponse({"data": schedule})
    else:
        return HttpResponseBadRequest()

def genSummary(request: HttpRequest) -> HttpResponse:
    todos = getTodoList()
    schedule = models.Schedule.objects.get(pk=1)
    summary = ai.Gen.genSummary(data=str({"task": todos, "schedule": schedule.content}))
    models.TodoSummary.objects.create(content=summary)
    return JsonResponse({"data": summary})
