from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "whatisthis?"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1 and len(request.form['comment']) < 1:
        flash('Please enter your name and a comment')
        return redirect('/')
    elif len(request.form['name']) < 1:
        flash('Please enter a name.')
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash('Please enter a comment.')
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash('Your comment is too long!')
        return redirect('/')
    name = request.form['name']
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    comment = request.form['comment']

    return render_template("dojo_survey_results.html", name=name, loc=dojo_loc, fav=fav_lang, comment=comment)
app.run(debug=True)
