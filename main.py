from flask import Flask
from simplepage import simple_page

app = Flask(__name__)

app.register_blueprint(simple_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

