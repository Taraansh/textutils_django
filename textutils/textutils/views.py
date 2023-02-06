# Created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse('capitalize first <button><a href="/">Back</a></button> ')
#
#
# def newlineremove(request):
#     return HttpResponse('new line remove <button><a href="/">Back</a></button> ')
#
#
# def spaceremove(request):
#     return HttpResponse('space remove <button><a href="/">Back</a></button> ')
#
#
# def charcount(request):
#     return HttpResponse('charcount <button><a href="/">Back</a></button> ')
