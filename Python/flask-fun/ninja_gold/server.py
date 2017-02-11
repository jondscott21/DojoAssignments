from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random
from datetime import datetime


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = ""
    print request.form['building']
    session['choice'] = request.form['building']
    choice = session['choice']
    if choice == 'farm':
        session['farmgold'] = random.randrange(10, 21)
        session['gold'] = int(session['gold']) +session['farmgold']
        session['log'] += "Earned " + str(session['farmgold']) + " gold from the farm!" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']
    if choice == 'cave':
        session['cavegold'] = random.randrange(5, 11)
        session['gold'] = int(session['gold']) + session['cavegold']
        session['log'] += "Earned " + str(session['cavegold']) + " gold from the cave!" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']
    if choice == 'house':
        session['housegold'] = random.randrange(1, 6)
        session['gold'] = int(session['gold']) + session['housegold']
        session['log'] += "Earned " + str(session['housegold']) + " gold from the house!" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print session['gold']
    if choice == 'casino':
        session['casinogold'] = random.randrange(-50, 51)
        session['gold'] = int(session['gold']) + session['casinogold']
        session['log'] += "Earned " + str(session['casinogold']) + " gold from the casino!" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n"
        print random.randrange(-50, 51)
        print session['gold']


    return redirect('/')

app.run(debug=True)
