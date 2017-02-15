# pair programmed with Arnold Son
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
from time import strftime
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'ThisIsSecret'


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
    query1 = 'SELECT * FROM messages'
    message = mysql.query_db(query1)
    query2 = 'SELECT messages.id as id, concat(first_name, " ", last_name) as name, message, messages.created_at as created_at from users join messages on users.id = messages.user_id'
    user_name = mysql.query_db(query2)
    query3 = 'select concat(first_name, " ", last_name) as commenter, comments.created_at as created, message_id, comment from users join comments on users.id = comments.user_id'
    comment = mysql.query_db(query3)
    print comment
    return render_template('index.html', all_messages=message, user_name=user_name, all_comments=comment)


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
    return redirect('/')
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


@app.route('/log_out', methods=['get'])
def log_out():
    session.clear()
    return redirect('/')
@app.route('/message', methods=['post'])
def message():
    if 'user' in session:
        query = "INSERT INTO messages (message,  created_at, updated_at, user_id) values (:message, now(), now(), :user_id);"
        data = {
            'message': request.form['message'],
            'user_id': session['user'],
        }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        flash('Please log in to post a message!')
        return redirect('/')
@app.route('/comment', methods=['post'])
def comment():
    if 'user' in session:
        query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) values (:message_id, :user_id, :comment, now(), now())"
        data = {
            'comment': request.form['comment'],
            'user_id': session['user'],
            'message_id': request.form['messageid']
        }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        flash('Please log in to post a comment!')
        return redirect('/')


@app.route('/delete/<del_id>')
def delete(del_id):
    query1 = 'delete from comments where message_id = :id'
    data1 = {'id': del_id}
    mysql.query_db(query1, data1)
    query2 = "DELETE FROM messages WHERE id = :id"
    data2 = {'id': del_id}
    mysql.query_db(query2, data2)
    return redirect('/')
app.run(debug=True)
