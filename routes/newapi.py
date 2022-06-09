from flask import Flask, Blueprint, render_template, redirect, send_from_directory
import os

bl_api2 = Blueprint('api2', __name__)

currentversion = 'v1'

@bl_api2.route('/api/<string:version>/<string:section>/<string:subdir>/<string:path>')
def index(version, section, subdir, path):
    fdir = 'api' + '/' + version + '/' + section + '/' + subdir + '/'
    return send_from_directory(fdir, path)
