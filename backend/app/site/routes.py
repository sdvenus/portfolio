from flask import Blueprint,render_template
site = Blueprint('site',__name__,template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/personal-information')
def profile():
    return render_template('profile.html')

@site.route('/background')
def background():
    return render_template('background.html')
