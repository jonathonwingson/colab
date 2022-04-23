from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json


profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
def printTable():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs = jobs)