from flask import Flask, Blueprint, render_template, redirect, send_from_directory
from markupsafe import escape
import os

bl_test = Blueprint('test', __name__)

@bl_test.route('/api/v1/exploit/test')
def index():
    return os.urandom(16)
