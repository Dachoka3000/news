import urllib.request, json
from .models import News, Source



api_key = None

headlines_base_url = None
sources_base_url = None
everything_base_url = None

def configure_request(app):
    global api_key, headlines_base_url, sources_base_url, everything_base_url
    api_key = app.config['NEWS_API_KEY']
    headlines_base_url = app.config['TOP_HEADLINES_BASE_URL']
    sources_base_url = app.config['SOURCES_BASE_URL']
    everything_base_url = app.config['EVERYTHING_BASE_URL']

def get_news(article):
    '''
    function that gets the json response to our url request
    '''
    get_news_url = everything_base_url.format(article,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news_results(news_results_list)
    return news_results

def process_news_results(news_list):
    '''
    function that processes the news result and transforms them into a list of objects
    
    Args:
        news_list: a list of dictionaries that contain news details
    Returns:
        news_results: a list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

    if description:
        news_object = News(title, description, url, urlToImage, publishedAt)
        news_results.append(news_object)

    return news_results

def get_source(category):
    '''
    functiion that gets the json response to the url request
    '''
    get_source_url = sources_base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_source_results(source_results_list)
    
    return source_results

def process_source_results(source_list):
    '''
    function that processes the source result and transform them into a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        if url:
            source_object = Source(id, name, url, category, language)
            source_results.append(source_object)

    return source_results

def get_source_news(id):
    '''
    function that gets the json response to our url response
    '''
    get_source_news_url = headlines_base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_news_url) as url:
        get_source_news_data = url.read()
        get_source_news_response = json.loads(get_source_news_data)

        source_news_results = None

        if get_source_news_response['articles']:
            source_news_list = get_source_news_response['articles']
            source_news_results = process_source_news_results(source_news_list)

    return source_news_results

def process_source_news_results(source_news_list):
    '''
    function that processes the news result and transforms them into a list of objects
    
    Args:
        news_list: a list of dictionaries that contain news details
    Returns:
        news_results: a list of news objects
    '''
    source_news_results = []
    for source_news_item in source_news_list:
        title = source_news_item.get('title')
        description = source_news_item.get('description')
        url = source_news_item.get('url')
        urlToImage = source_news_item.get('urlToImage')
        publishedAt = source_news_item.get('publishedAt')

    if title:
        source_news_object = News(title, description, url, urlToImage, publishedAt)
        source_news_results.append(source_news_object)

    return source_news_results

    



