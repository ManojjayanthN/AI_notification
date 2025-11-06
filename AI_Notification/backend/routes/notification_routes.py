from flask import Blueprint, jsonify
from backend.models.notification_log_model import db, NotificationLog

notification_bp = Blueprint("notification_bp", __name__)

@notification_bp.route("/logs", methods=["GET"])
def get_logs():
    logs = NotificationLog.query.all()
    return jsonify([
        {
            "id": l.id,
            "user_id": l.user_id,
            "event_id": l.event_id,
            "timestamp": l.timestamp,
            "delivery_status": l.delivery_status,
            "opened": l.opened
        } for l in logs
    ])
