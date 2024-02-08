from flask import Flask
from src.main.routes.tag_route import route_bp

app = Flask(__name__)

app.register_blueprint(route_bp)