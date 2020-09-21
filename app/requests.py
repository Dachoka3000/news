from app import app
import urllib.request, json
from .models import news

api_key = app.config['NEWS_API_KEY']

headlines_base_url = app.config['TOP_HEADLINES_BASE_URL']
sources_base_url = app.config['SOURCES_BASE_URL']
everything_base_url = app.config['EVERYTHING_BASE_URL']

def get_news(title):
    '''
    function that gets the json response to our url request
    '''
    get_news_url = headlines_base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']

