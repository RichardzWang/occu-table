#Richard Wang
#9/22/16
#Period 9



from utils import occupations
from flask import Flask, render_template



occulist = occupations.parseCSV("data/occupations.csv")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html', message = "Hello")

@app.route("/occupations/")
def occupation():
    return render_template('occupations.html', dictionary = occulist, future = occupations.choose(occulist))

    

if __name__ == '__main__':
    app.debug = True
    app.run()
