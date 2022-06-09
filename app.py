from flask import Flask
from routes.root import *
from routes.api import *
from routes.lol import *
from routes.newapi import *

app = Flask(__name__)
app.register_blueprint(bl_root)
app.register_blueprint(bl_api)
app.register_blueprint(bl_lol)
app.register_blueprint(bl_api2)