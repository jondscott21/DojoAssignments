from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    if request.session['num'] > 0:
        request.session['stuff'] = get_random_string(length=14)

    return render(request, 'index.html')
def increase(request):
    request.session['num'] += 1 
    return redirect('/')
# tri-programmed by arnold son, jon scott, le lin
