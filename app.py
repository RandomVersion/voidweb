from flask import Flask
from routes.root import *
from routes.api import *
from routes.testapi import *
from routes.lol import *

app = Flask(__name__)
app.register_blueprint(bl_root)
app.register_blueprint(bl_api)
app.register_blueprint(bl_test)
app.register_blueprint(bl_lol)