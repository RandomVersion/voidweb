from flask import Blueprint, render_template, redirect

bl_root = Blueprint('root', __name__)

@bl_root.route('/')
def index():
    return render_template("root.html")
