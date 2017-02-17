from django.shortcuts import render, redirect, HttpResponse
from random import randrange
from time import localtime, strftime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'ninjaGold/index.html')
def process(request, building):
    if building == 'farm':
        request.session['gains'] = randrange(10, 21)
        request.session['gold'] += request.session['gains']

        print request.session['gold']
    elif building == 'cave':
        request.session['gains'] = randrange(5, 11)
        request.session['gold'] += request.session['gains']
        print request.session['gold']
    elif building == 'house':
        request.session['gains'] = randrange(2, 6)
        request.session['gold'] += request.session['gains']
        print request.session['gold']
    elif building == 'casino':
        request.session['gains'] = randrange(-50, 50)
        request.session['gold'] += request.session['gains']
    if request.session['gains'] < 0:
        request.session['log'].append("Entered a casino and lost " + str(request.session['gains']) + " gold... Ouch... " + strftime("%b %d, %Y %I:%M:%S %p", localtime()))
    elif request.session['gains'] == 0:
        request.session['log'].append("Entered a casino and broke even. " + strftime("%b %d, %Y %I:%M:%S %p", localtime()))
    else:
        request.session['log'].append("Earned " + str(request.session['gains']) + " gold from the " + building + "! " + strftime("%b %d, %Y %I:%M:%S %p", localtime()))
        print request.session['log']
    return redirect('/')