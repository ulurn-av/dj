from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse, Http404


def index(request):
    return HttpResponse("Hello")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    print(request.POST)
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):

    # if year > 2023:
    #     raise Http404()
    if year > 2023:
        redirect('/')
    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Not Foun</h1>")