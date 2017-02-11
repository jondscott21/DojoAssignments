from flask import Flask, redirect, render_template

from email_valid.mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)
