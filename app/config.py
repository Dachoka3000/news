class Config:
    '''
    general configuration parent class
    '''
    pass

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