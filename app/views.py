from flask import render_template
from app import app
from process_text import ten_abbs, search_string

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/headers')
def headers():
    return render_template('headers.html', abb_list = ten_abbs)

@app.route('/search/', defaults={'search_term': None})
@app.route('/search/<string:s>')
def search(search_term = None):
    search_results = search_string(search_term)
    return render_template('search.html', results = search_results)


