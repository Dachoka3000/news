import unittest
from app.models import Source

class NewsTest(unittest.TestCase):
    '''
    test class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Source("1234","abc news","https://abcnews.go.com","business","en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))