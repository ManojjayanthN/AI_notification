from flask import Blueprint, jsonify, request
from backend.models.event_model import db, Event
from backend.modules.utils import parse_datetime

event_bp = Blueprint("event_bp", __name__)

@event_bp.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([{"id": e.id, "name": e.name, "deadline": e.deadline, "urgency": e.urgency} for e in events])

@event_bp.route("/events", methods=["POST"])
def add_event():
    data = request.json
    new_event = Event(
        name=data['name'],
        deadline=parse_datetime(data['deadline']),
        urgency=data['urgency']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"status": "success"}), 201
