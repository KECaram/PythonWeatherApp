#!/usr/bin/python
# Keith Caram
# INFO.305.061: Survey of Python, Perl, and PHP
# Assignment #4 - Complex Python Program
#                               Program Summary
#This is a tiny bit of test code. I wrote test code that checks if my home page loads
#and that the page loads with the correct header. I could not figure out how to check how
#the 'POST' worked on my page and loading a new page.

import unittest
from weatherWebApp import app
import unittest

class FlaskWeatherAppTest(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_home_content(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type= 'html/text')
            self.assertTrue(b'Weather Dashboard' in response.data)

if __name__ == '__main__':
    unittest.main()
