from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random


@app.route('/')
def index():
    if 'win' not in session:
        session['win'] = random.randrange(0, 101)
    return render_template('index.html')


@app.route('/game', methods=['POST'])
def game():
    session['guess'] = int(request.form['guess'])
    if session['guess'] == session['win']:
        session['result'] = str(session['guess']) + ' is the winning number!'
        print 'win'
    elif session['guess'] > session['win']:
        session['result'] = str(session['guess']) + ' is too high'
        print 'too high'
    elif session['guess'] < session['win']:
        session['result'] = str(session['guess']) + ' is too low'
        print 'too low'
    return redirect('/')


@app.route('/winner')
def win():
    print 'stuff'
    session.pop('win')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
