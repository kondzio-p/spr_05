from django.shortcuts import render

# Create your views here.

def spr05(request):
    context = {}
    return render(request, 'Apka05/spr05.html', context)