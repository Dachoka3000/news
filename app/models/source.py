class Source:
    '''
    This is a class that defines source objects
    '''

    def __init__(self,id,name,url,category,language):
        '''
        init method to initialize new source objects

        Args:
            id: id of the news source
            name: name of the news source organization
            url: url of the news organization
            category: categories of news covered by that organisation
            language: reporting language of that news source
        '''
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        self.language = language