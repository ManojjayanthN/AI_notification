from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class NotificationLog(db.Model):
    __tablename__ = 'notification_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    delivery_status = db.Column(db.String(20))
    opened = db.Column(db.Boolean, default=False)
