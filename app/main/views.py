from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_source, get_news, get_source_news

#views
@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    general = get_source('general')
    # entertainment = get_source('entertainment')
    # business = get_source('business')
    # health = get_source('health')
    title = 'News Today'
    return render_template('index.html', title = title, general = general)

@main.route('/technews')
def techienews():
    '''
    view  technews page function that returns the news details page and its data
    '''
    technology = get_news('technology')
    title = 'Tech News'
    return render_template('technews.html',title = title, technology= technology)

@main.route('/economy')
def economynews():
    '''
    view economy news page function that returns economy news details
    '''
    economy = get_news('business')
    title = 'Economy news'
    return render_template('econ.html',title = title, economy = economy )

@main.route('/source/<id>')
def news(id):
    '''
    view news function that returns articles page function and its data
    '''
    article_list = get_source_news(id)
    title = f'{id}'

    return render_template('articles.html', title = title, article_list= article_list)

