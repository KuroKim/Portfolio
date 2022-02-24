from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def index(request):
    return HttpResponse("Портфолио")


