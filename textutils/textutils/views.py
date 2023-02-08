# Created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`=+-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'CAPITALIZED', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ''
        # for char in djtext:
        #     if char != '\n':
        #         analyzed = analyzed + char
        analyzed = djtext.replace('\n', '')
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if index + 1 < len(djtext) and (not (djtext[index] == " " and djtext[index + 1] == " ")):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcounter == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')
