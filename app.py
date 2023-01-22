from flask import Flask
from flask_sslify import SSLify

from routes.api import api

app = Flask(__name__)
sslify = SSLify(app)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run()