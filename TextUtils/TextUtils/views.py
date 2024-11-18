from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charCounter=request.GET.get('charCounter','off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    # Analyze the text

        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed ExtraSpace', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(charCounter=="on"):
        analyzed = ""
        char_count = 0 

        for char in djtext:
            if char != " ":  # Exclude spaces from the character count
                char_count += 1
                analyzed += char  

    # Prepare the parameters for rendering
        params = {
            'purpose': 'Character Counter',
            'analyzed_text': analyzed,
            'char_count': char_count,  
            }

        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

