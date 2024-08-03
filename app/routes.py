from flask import Blueprint, render_template, jsonify, request
from . import db
from .models import Conference
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/conferences', methods=['GET'])
def get_conferences():
    conferences = Conference.query.all()
    return jsonify([conf.to_dict() for conf in conferences])

@bp.route('/api/conferences', methods=['POST'])
def create_conference():
    data = request.json
    new_conference = Conference(name=data['name'], date=data['date'])
    db.session.add(new_conference)
    db.session.commit()
    return jsonify(new_conference.to_dict()), 201
