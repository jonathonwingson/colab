from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json


logout_views = Blueprint('logout_views', __name__, template_folder='../templates')

@logout_views.route('/logout')
def logout():
    logout_user()
    return render_template('jobs.html')
