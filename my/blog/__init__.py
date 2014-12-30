from pyramid.config import Configurator


def includeme(config):
    config.add_route('top', '/')
    config.scan(".views")


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_mako')
    config.include('pyramid_tm')
    config.include('.')
    return config.make_wsgi_app()
