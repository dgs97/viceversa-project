from django.shortcuts import render 

def home(request):
    return render(request,'home.html')

def reverse(request):
    text = request.GET["usertext"]
    text_reverse = text[::-1]
    return render(request,'reverse.html',{"usertext":text,"reversetext":text_reverse})