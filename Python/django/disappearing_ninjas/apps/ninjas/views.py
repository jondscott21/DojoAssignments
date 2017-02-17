from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')


def ninjas(request):

    return render(request, 'ninjas/ninjas.html')


def turtle(request, color):
    if color == 'purple':
        context = {
            "turtle": "ninjas/images/donatello.png"
        }
    elif color == 'blue':
        context = {
            "turtle": "ninjas/images/leonardo.png"
        }

    elif color == 'red':
        context = {
            "turtle": "ninjas/images/raphael.png"
        }
    elif color == 'orange':
        context = {
            "turtle": "ninjas/images/michelangelo.png"
        }
    else:
        context = {
            "turtle": "ninjas/images/fox.jpg"
        }

    return render(request, 'ninjas/turtle.html', context)