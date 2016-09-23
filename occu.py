#Richard Wang
#9/22/16
#Period 9

import profession.py
from Flask import flask, render_template

poslist = profession.reader("occupations.csv")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html', message = "Hello")

@app.route("/occupations")
def occupation():
    return render_template('occupations.html', posoccupations = poslist,
occupation = profession.choose(poslist))
    

if __name__ == '__main__':
    app.debug = True
    app.run()
