from flask import Flask
from blueprints.main_site import main_site

app = Flask(__name__)

app.register_blueprint(main_site)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
