from api import models
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpRequest
from django.db.models import Model
from django import forms

class BaseView():
    def __init__(self, model: Model) -> None:
        self.model = model
        class Form(forms.ModelForm):
            class Meta:
                model = self.model
                fields = "__all__"
        self.Form = Form
    
    def addView(self, request: HttpRequest) -> HttpResponse:
        form = self.Form(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            self.model.objects.create(**data)
        else:
            return HttpResponseBadRequest()
        return HttpResponse()
    
    def editView(self, request: HttpRequest) -> HttpResponse:
        form = self.Form(request.GET)
        if form.is_valid() and request.GET.get("id"):
            data = form.cleaned_data
            self.model.objects.update(pk=int(request.GET["id"]), **data)
        else:
            return HttpResponseBadRequest()
        return HttpResponse()
    
    def deleteView(self, request: HttpRequest) -> HttpResponse:
        if request.GET.get("id"):
            self.objects.delete(pk=int(request.GET["id"]))
        else:
            return HttpResponseBadRequest()
        return HttpResponse()

TodoView = BaseView(models.Todo)
HabitView = BaseView(models.Habit)
TagView = BaseView(models.Tag)
