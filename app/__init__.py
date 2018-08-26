from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
config = app.config

from app import routes

if __name__ == "__main__":
    app.run()
