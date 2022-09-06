from django.shortcuts import render
def index(request):
    return render(request, 'home.html')

def index1(request):
    return render(request, 'about.html')