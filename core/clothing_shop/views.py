from django.shortcuts import render

def index(request):
    return render(request, 'clothing_shop/index.html')
