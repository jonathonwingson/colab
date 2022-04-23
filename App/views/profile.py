from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json

from flask_login import login_required, current_user

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')


@profile_views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)