from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # to check out the homepage
        self.browser.get('http://localhost:8000')
        # the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        #to enter a to-do items
        # User types an item and updates
        # types and updates again
        # site generated a unique URL for users
        # Try another browser to visit and check is there still the lists


if __name__ == '__main__':
    unittest.main(warnings='ignore')
