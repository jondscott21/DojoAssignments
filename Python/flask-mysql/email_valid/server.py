from flask import Flask, render_template, request, redirect, session, flash

from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'valid_emails')
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@app.route('/')
def index():
    query = 'select'
    return render_template('index.html')


@app.route('/email', methods=['post'])
def email_1():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email not valid')
        return redirect('/')
    else:
        flash('The email address you entered' + request.form['email'] + ' is a VALID email address! Thank you!')
        query = "insert into emails(email, created_at) values(:email, NOW())"
        data = {
        'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)
app.run(debug=True)
