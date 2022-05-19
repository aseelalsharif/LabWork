from django.shortcuts import render

# Create your views here.

def Malaysia(request):
    return render(request, 'Gallery/Malaysia.html')

def Turkey(request):
    return render(request, 'Gallery/Turkey.html')