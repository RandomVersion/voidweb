from flask import Blueprint, render_template, send_from_directory

bl_root = Blueprint('root', __name__)

@bl_root.route('/')
def index():
    return send_from_directory('static', 'index.html')