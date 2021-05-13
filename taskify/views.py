from .models import ToDo
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_manager
from . import db


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
        todo = request.form.get('todo')
        #notes = request.form.get('notes')    

        new_todo = ToDo(todo_list=todo, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()

    return render_template('home.html', user=current_user)

@views.route('/kanban')
@login_required
def kanban():
    return render_template('kanban.html', user=current_user)

@views.route('/calendar')
@login_required
def calendar():
    events = [
        {
            'todo' : "testing",
            'date' : "2021-05-14"
        },
        {
            'todo' : 'eat',
            'date' : '2021-05-15'
        }
    ]

    return render_template('calendar.html', user=current_user, events=events)