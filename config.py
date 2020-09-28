import os

class Config:
    '''
    general configuration parent class
    '''
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey=d23ab82d7eb3439ca11458234be3769e'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = 'd23ab82d7eb3439ca11458234be3769e'

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: the parent configuratiion class with general settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}