import unittest
import webtest
from testfixtures import compare


class TestApp(unittest.TestCase):
    def test_it(self):
        from my.blog import main
        app = main({})
        app = webtest.TestApp(app)
        res = app.get("/")
        compare(res.text, "Hello")
