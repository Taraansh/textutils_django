# Created by me
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")


def removepunc(request):
    return HttpResponse('remove punc <button><a href="/">Back</a></button> ')


def capfirst(request):
    return HttpResponse('capitalize first <button><a href="/">Back</a></button> ')


def newlineremove(request):
    return HttpResponse('new line remove <button><a href="/">Back</a></button> ')


def spaceremove(request):
    return HttpResponse('space remove <button><a href="/">Back</a></button> ')


def charcount(request):
    return HttpResponse('charcount <button><a href="/">Back</a></button> ')
