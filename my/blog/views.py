from pyramid.view import view_config
from pyramid_deform import FormView
from colanderalchemy import SQLAlchemySchemaNode
from .models import Blog


@view_config(route_name="top", renderer="templates/index.mako")
def index(request):
    blog = Blog.query.filter(Blog.name == 'default').one()
    return dict(blog=blog)


@view_config(route_name="config", renderer="templates/config.mako")
class BlogConfigView(FormView):
    schema = SQLAlchemySchemaNode(Blog, excludes=["id", "name"])
    buttons = ("save",)
    def save_success(self, values):
        blog = Blog.query.filter(Blog.name == 'default').one()
        blog.description = values["description"]

