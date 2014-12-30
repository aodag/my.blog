from pyramid.view import view_config
from .models import Blog


@view_config(route_name="top", renderer="templates/index.mako")
def index(request):
    blog = Blog.query.filter(Blog.name == 'default').one()
    return dict(blog=blog)
