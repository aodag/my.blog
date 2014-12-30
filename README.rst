===========================
my.blog
===========================

INSTALL
===========================

``my.blog`` is wsgi application.
That isn't packaging project.

::

  $ git clone git@github.com:aodag/my.blog.git
  $ pip install -r requirements.txt -f wheelhouse --no-index
  $ alembic upgrade head
  $ pserve demo.ini
