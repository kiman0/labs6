from .containers import ApplicationContainer


def create_app():
    container = ApplicationContainer()
    container.config.from_yaml('config.yml')

    app = container.app()
    app.container = container
    
    app.add_url_rule('/', view_func=container.index_view.as_view())
    app.add_url_rule('/health', view_func=container.health_view.as_view())

    return app