from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def main(request):
    return render(request, 'it/index.html')


def demand(request):
    return render(request, 'it/demand.html')


def geo(request):
    return render(request, 'it/geo.html')


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>К сожалению, страница не найдена ¯\_(ツ)_/¯</h1>')