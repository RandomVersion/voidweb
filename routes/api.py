from flask import Flask, Blueprint, render_template, redirect, send_from_directory
from markupsafe import escape
import os

bl_api = Blueprint('api', __name__)

pathlist = ['users', 'troll', 'exploit', 'grab']

currentversion = 'v1'

@bl_api.route('/api/<string:version>/<string:section>/<string:path>')
def index(version, section, path):
    fdir = 'api' + '/' + version + '/' + section + '/'
    return send_from_directory(fdir, path)