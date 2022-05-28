import requests
import json
from flask import Flask, render_template, request

url_history = 'http://hn.algolia.com/api/v1/search?query=foo&tags=story'
url_popular = 'https://hn.algolia.com/api/v1/search?tags=story'
url_id = 'http://hn.algolia.com/api/v1/items/{id}'


app = Flask('maratona_news')

@app.route('/')
def index():
    order_by = request.args.get('order_by')
    if order_by == 'news':
        url = 'http://hn.algolia.com/api/v1/search?query=foo&tags=story'
    else:
        url = 'https://hn.algolia.com/api/v1/search?tags=story'

    resultados = requests.get(url).json()
    resultados = resultados['hits']


    return render_template('index.html',resultados = resultados)

@app.route('/<id>')
def by_id():
    url = f'http://hn.algolia.com/api/v1/items/{id}'
    resultados = requests.get(url).json()
    return render_template('id.html', resultados = resultados)

# @app.route('/<id>')
# def by_id(id):
#   url = f"http://hn.algolia.com/api/v1/items/{id}"
#   resultados = requests.get(url).json()
#   return render_template('id.html', resultados=resultados)




if  __name__  ==  '__main__':
    app.run()

#
