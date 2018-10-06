from django.shortcuts import render

def  home(request):
    return render(request, '../templates/site/home.html')
