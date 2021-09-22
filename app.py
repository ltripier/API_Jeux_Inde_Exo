from flask import Flask, render_template , request
import requests


url = "https://tastedive.com/api/similar?"
key = "423979-David-BAQ5JQRC"
type_res = "games" #  music, movies, shows, podcasts, books, authors, games
info = str(1) # when set to 1, additional information is provided, like a description and a related Youtube clip (when available). 
            # Default is 0.

app = Flask(__name__)

title='H API Game'
@app.route('/')
def index():
    return render_template('index.html', title=title)

@app.route('/search', methods=['POST'])
def search():
    inputVal = request.form["search-bar"]
    q = inputVal
    param = f"q={q}" + "&" + f"type={type_res}" + "&" + f"info={info}" + "&" + f"k={key}"
    qry = url + param
    r = requests.get(qry).json()

    return render_template('search.html', r=r)   


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)
    
    