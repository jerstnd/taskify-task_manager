from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def landing_page():
    return render_template('landingpage.html', user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        lists = request.form.get('todo')
        notes = request.form.get('notes')
    return render_template('home.html', user=current_user)
