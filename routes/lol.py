from flask import Flask, Blueprint, redirect

bl_lol = Blueprint('lol', __name__)

# do some trolling

@bl_lol.route('/lol')
def index():
    return redirect('about:neterror', code=302)