# pair programmed with Arnold Son
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_reg')
app.secret_key = 'ThisIsSecret'
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASSWORD_REGEX = re.compile(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,})', re.MULTILINE)
name_regex = re.compile(r'([a-zA-Z]{2,})', re.MULTILINE)


@app.route('/')
def index():
    if 'user' in session:
        user_query = "select first_name, last_name from users where id = :id"
        user_data = {
            'id': session['user']
        }
        query = mysql.query_db(user_query, user_data)
        flash('You are logged in as ' + query[0]["first_name"] + " " + query[0]["last_name"])
    return render_template('index.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    if not name_regex.match(request.form['first_name']):
        flash('First Name must be letters only and at least two characters')
        return redirect('/')
    else:
        first_name = request.form['first_name']
    if not name_regex.match(request.form['last_name']):
        flash('Last Name must be letters only and at least two characters')
        return redirect('/')
    else:
        last_name = request.form['last_name']
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        return redirect('/')
    else:
        email = request.form['email']
    if not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must be at least 8 characters and have at least 1 uppercase letter and 1 number')
        return redirect('/')
    if not request.form['confirm'] == request.form['password']:
        flash('Password does not match')
        return redirect('/')
    else:
        password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
    query_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pw_hash': pw_hash
    }
    mysql.query_db(insert_query, query_data)
    return render_template('/info')
@app.route('/validation', methods=['post'])
def validation():
    print 'did it!!!'
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        session['user'] = user[0]['id']
        print session['user']
    else:
        flash('Log in failed')
    return redirect('/')
app.route('/info', methods=['get'])
app.run(debug=True)
