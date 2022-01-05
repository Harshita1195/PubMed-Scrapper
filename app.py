# import the required libraries
from flask import Flask, render_template, request, jsonify, Response, url_for, redirect
from flask_cors import CORS, cross_origin
import pandas as pd
import csv, json
from scrapping import scrapper

app = Flask(__name__)  # initialising the flask app with the name 'app'

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        searchString = request.form['content']
        expected_articles = int(request.form['expected_articles'])
        scrapper(expected_articles, searchString)
        
        with open('static/articles.csv', encoding="utf8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        with open('static/articles.json','w') as f:
            json.dump(rows, f)
        f = open('static/articles.json')
        data = json.load(f)

        return render_template('results.html', data=data)

    else:
        return render_template('index.html')
        
if __name__=='__main__':
    app.run(debug=True)
