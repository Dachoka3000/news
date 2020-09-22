from flask import render_template
from app import app
from .requests import get_news, get_source

#views
@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    general = get_source('general')
    entertainment = get_source('entertainment')
    business = get_source('business')
    health = get_source('health')
    title = 'News Today'
    return render_template('index.html', title = title, general = general, entertainment = entertainment, business = business, health = health)

@app.route('/news/business')
def news():
    '''
    view news page function that returns the news details page and its data
    '''
    return render_template('news.html')