from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Incident, User
from . import db
from .email_utils import send_email

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    incidents = Incident.query.all()
    return render_template('dashboard.html', incidents=incidents)

@bp.route('/incident/new', methods=['GET', 'POST'])
@login_required
def create_incident():
    if request.method == 'POST':
        incident = Incident(
            title=request.form['title'],
            description=request.form['description'],
            created_by=current_user.username
        )
        db.session.add(incident)
        db.session.commit()
        send_email("New Incident Logged", f"A new incident was created: {incident.title}")
        return redirect(url_for('routes.dashboard'))
    return render_template('create_incident.html')

@bp.route('/incident/<int:id>', methods=['GET', 'POST'])
@login_required
def view_incident(id):
    incident = Incident.query.get(id)
    if request.method == 'POST':
        incident.status = request.form['status']
        incident.assigned_to = request.form['assigned_to']
        db.session.commit()
        send_email("Incident Updated", f"Incident {incident.title} updated.")
        return redirect(url_for('routes.dashboard'))
    return render_template('view_incident.html', incident=incident)
