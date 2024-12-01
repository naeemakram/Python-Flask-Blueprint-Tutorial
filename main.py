from flask import Flask
from blueprints.main_site import main_site

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_site.main_site)
    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
