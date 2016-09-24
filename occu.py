#Richard Wang
#9/22/16
#Period 9



import csv, random
from flask import Flask, render_template



def parseCSV(filename):
    with open(filename, "r") as raw:
        reader = csv.reader(raw)
        parsed = dict(reader)
        del parsed["Job Class"]
        return parsed

def choose(data):
    seed = random.random() * 99.8; # seed value
    for key in data:
        # print ( seed ) 
        seed -= float(data[key])
        if seed < 0:
            return key
    return -1



occulist = parseCSV("occupations.csv")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html', message = "Hello")

@app.route("/occupations")
def occupation():
    return render_template('occupations.html', dictionary = occulist, future = choose(occulist))

    

if __name__ == '__main__':
    app.debug = True
    app.run()
