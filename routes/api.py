from flask import Flask, Blueprint, render_template, redirect, send_from_directory
import os

bl_api = Blueprint('api', __name__)
bl_api2 = Blueprint('api2', __name__)

currentversion = 'v1'

@bl_api.route('/api/<string:version>/<string:section>/<string:path>')
def index(version, section, path):
    fdir = 'api' + '/' + version + '/' + section + '/'
    return send_from_directory(fdir, path)

@bl_api2.route('/api/<string:version>/<string:section>/<string:subdir>/<string:path>')
def index(version, section, subdir, path):
    fdir = 'api' + '/' + version + '/' + section + '/' + subdir + '/'
    return send_from_directory(fdir, path)
