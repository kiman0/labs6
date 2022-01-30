from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask

from . import views, services


class ApplicationContainer(containers.DeclarativeContainer):

    app = flask.Application(Flask, __name__)
    
    config = providers.Configuration()

    env = providers.Factory(
        services.Enviroment,
        env=config.env
    )
    
    index_view = flask.View(views.index)
    health_view = flask.View(
        views.health,
        enviroment=env
    )