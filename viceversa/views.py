from posixpath import split
from django.shortcuts import render 

def home(request):
    return render(request,'home.html')

def reverse(request):
    text = request.GET["usertext"]
    count_of_words = len(text.split())
    text_reverse = text[::-1]
    return render(request,'reverse.html',{"countwords":count_of_words,"usertext":text,"reversetext":text_reverse})