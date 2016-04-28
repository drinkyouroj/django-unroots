from django.shortcuts import render

def index(request):
    """The home page for unroots LL"""
    return render(request, 'll_app/index.html')
