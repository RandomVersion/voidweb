from flask import Flask, Blueprint, render_template, redirect
from markupsafe import escape

bl_deny = Blueprint('deny', __name__)

@bl_deny.route('/api/')
def v1(version, section, path):
    return redirect('/')