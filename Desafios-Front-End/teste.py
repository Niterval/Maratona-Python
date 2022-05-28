
import requests
from flask import Flask, render_template, request

url_history = 'http://hn.algolia.com/api/v1/search?query=foo&tags=story'
url_popular = 'https://hn.algolia.com/api/v1/search?tags=story'
url_id = 'http://hn.algolia.com/api/v1/items/{id}'



app  =  Flask ('Matatona News')

@app.route ( '/' )
def  hello_world ():
    return  'Hello World!'

if  __name__  ==  '__main__' :
    app.run()
