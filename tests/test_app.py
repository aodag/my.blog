import os
import unittest
import webtest
from testfixtures import compare


settings = {
    "sqlalchemy.url": os.getenv("DATABASE_URL"),
}


class TestApp(unittest.TestCase):
    def setUp(self):
        import transaction
        from my.blog import main
        from my.blog import models
        app = main({}, **settings)
        models.Base.metadata.drop_all()
        models.Base.metadata.create_all()
        blog = models.Blog(title="dummy blog", name="default")
        models.DBSession.add(blog)
        transaction.commit()
        self.app = webtest.TestApp(app)

    def tearDown(self):
        from my.blog import models
        models.Base.metadata.drop_all()

    def test_it(self):
        self.app.get("/")
        res = self.app.get("/config")
        res.form["description"] = "updated"
        res = res.form.submit("save")
        compare(res.form["description"].value, "updated")
        res = self.app.get("/")
        assert "updated" in res
