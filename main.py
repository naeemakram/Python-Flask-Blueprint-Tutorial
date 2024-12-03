from flask import Flask
from blueprints import main_site
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(main_site.main_site)
    print(f'App name: {__name__}', f'Instance path is: {app.instance_path}')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
