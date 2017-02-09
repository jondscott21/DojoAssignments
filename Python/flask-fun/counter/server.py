from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    if 'counter' not in session:
        session['counter'] = 1
    return render_template("index.html", counter=1)


@app.route('/plus2')
def plus2():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset1')
def reset1():
    session['counter'] = 0
    return redirect('/')
app.run(debug=True)
