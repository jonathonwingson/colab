from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import Job, db
import json

from App.models import User
from flask_login import login_required, current_user, logout_user

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')


@profile_views.route('/profile', methods=['GET'])
@login_required
def profile():
    user = User.query.filter_by(email=current_user.email).first()
    return render_template('profile.html', user=user)

@profile_views.route('/delete/')
def delete():
    user = User.query.filter_by(email=current_user.email).first()
    logout_user()
    db.session.delete(user)
    db.session.commit()
    flash('Deleted Account')
    return render_template('index.html')