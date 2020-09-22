import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    test class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News("corona", "corona is a virus",'"https://fivethirtyeight.com/features/jamal-murray-isnt-the-new-steph-curry-but-he-might-be-close/', ' "https://fivethirtyeight.com/wp-content/uploads/2020/09/GettyImages-1094743508-e1600742098339.jpg?w=575','2020-09-22T18:00:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))