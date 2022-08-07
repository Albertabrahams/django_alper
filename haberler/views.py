from django.shortcuts import render

def index(request):
    return render(request, 'haberler/index.html')

