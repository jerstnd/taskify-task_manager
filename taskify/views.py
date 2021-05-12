from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_manager

views = Blueprint('views', __name__)

@views.route('/')
def landing_page():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    else:
        return render_template('landingpage.html', user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        lists = request.form.get('todo')
        notes = request.form.get('notes')
    return render_template('home.html', user=current_user)

@views.route('/scrum')
@login_required
def scrum():
    return render_template('scrum.html', user=current_user)
