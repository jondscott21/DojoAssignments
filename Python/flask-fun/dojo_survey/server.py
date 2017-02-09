from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def create_user():
    # return render_template("dojo_survey_results.html")
    print "Got Post Info"
    name = request.form['name']
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    return render_template("dojo_survey_results.html", name=name, loc=dojo_loc, fav=fav_lang)
    return redirect('/')
app.run(debug=True)
