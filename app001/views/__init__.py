# coding=utf-8
from django.http import HttpResponse


def customized404(request):
    return HttpResponse("找不到你要的东西的了，哎……")