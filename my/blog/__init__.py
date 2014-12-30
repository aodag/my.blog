from pyramid.config import Configurator


def hello(request):
    request.response.text = "Hello"
    return request.response


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_view(hello)
    return config.make_wsgi_app()
