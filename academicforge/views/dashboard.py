from flask import Blueprint, render_template
from flask_login import login_required

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard/index.html')
