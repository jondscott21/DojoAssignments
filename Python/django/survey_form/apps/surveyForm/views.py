from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'surveyForm/index.html')
def process(request):
    if request.method == 'POST':
        if 'count' in request.session:
            request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['loc'] = request.POST['loc']
        request.session['lang'] = request.POST['lang']
    return redirect('/result')
def result(request):
    return render(request, 'surveyForm/result.html')