class News:
    '''
    News class to define a news object
    '''

    def __init__(self,title, description, url, urlToImage, publishedAt):
        '''
        init method to initialize news article objects

        Args:
            title = title of the article
            descriiption = description of the article
            image = image of the article
            date = date that the article was published
        '''
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt