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

@app.route('/technews')
def techienews():
    '''
    view  technews page function that returns the news details page and its data
    '''
    technology = get_news('technology')
    title = 'Tech News'
    return render_template('technews.html',title = title, technology= technology)

@app.route('/economy')
def economynews():
    '''
    view economy news page function that returns economy news details
    '''
    economy = get_news('economy')
    title = 'Economy news'
    return render_template('econ.html',title = title, economy = economy )

@app.route('/news/<topic>')
def news(topic):
    '''
    view news function that returns articles page function and its data
    '''
    article = get_news(topic)
    title = f'{article.title}'

    return render_template('news.html', title = title, article=article)

