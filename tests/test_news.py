import unittest 
from app.models import Business, Sources, Everything, Headlines

class TestBusiness(unittest.TestCase):
    """
    TestBusiness sub-class defines test cases
    for the Business class behaviours.
    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a news_business_headlines instance
        before each test cases.
        """        
        self.news_business_headlines = Business("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")

    def test_instance(self):
        """
        This method will only assert if self.news_business_headlines is an instance of
        Business class.
                """
        self.assertTrue(isinstance(self.news_business_headlines, Business)) 


class TestSources(unittest.TestCase):
    """
    Test class that defines test cases 
    for the sources class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """
        Set up method to create a new_source instance
        before each test cases.
        """
        self.new_source = Sources("ABC-Z", "News Cast", "https://www.news-cast.com", "Kenya", "We provide in depth news from all around Kenya, with a 5 year experience..."  )

    def test_instance(self):
        """
        This method will only assert if self.new_source is an instance of
        Sources class.
        """
        self.assertTrue(isinstance(self.new_source, Sources))


class TestEverything(unittest.TestCase):
    """
    TestEverything sub-class defines test cases
    for the Everything class behaviours.
    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a everything_instance instance
        before each test cases.
        """        
        self.everything_instance = Everything("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")

    def test_instance(self):
        """
        This method will only assert if self.everything_instance is an instance of
        Everything class.
        """
        self.assertTrue(isinstance(self.everything_instance, Everything)) 

class TestHeadlines(unittest.TestCase):
    """
    TestHeadlines sub-class defines test cases
    for the Headlines class behaviours.
    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a news_headlines instance
        before each test cases.
        """        
        self.news_headlines = Headlines("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")


    def test_instance(self):
        """   
        This method will only assert if self.news_headlines is an instance of
        Headlines class.
        """
        self.assertTrue(isinstance(self.news_headlines, Headlines)) 




