from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#setup DB
db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)

    #Load config
    app.config.from_pyfile('settings.py')

    #apply overrides for tests
    app.config.update(config_overrides)

    #initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    #import blueprints
    from blog.views import blog_app
    from author.views import author_app

    #register blueprints
    app.register_blueprint(blog_app)
    app.register_blueprint(author_app)
    return app
