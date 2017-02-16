from django.shortcuts import render, HttpResponse
from time import strftime, localtime

# Create your views here.
def index(request):
    context = {
        "somekey": strftime("%b %d, %Y\n %I:%M:%S %p", localtime())
    }
    return render(request, 'timedisplay/index.html', context)