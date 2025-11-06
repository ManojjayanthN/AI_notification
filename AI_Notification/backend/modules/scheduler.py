import schedule
import time
from backend.modules.notification_sender import send_email
from backend.models import db_user, db_event, db_log, User, Event, NotificationLog

from datetime import datetime

def schedule_notifications(app):
    """Schedules notifications for all events every day at 09:00 AM"""
    with app.app_context():
        users = User.query.filter_by(role="student").all()
        events = Event.query.all()
        for user in users:
            for event in events:
                schedule.every().day.at("09:00").do(send_notification_task, user.id, event.id)

def send_notification_task(user_id, event_id):
    from backend.models import db, User, Event, NotificationLog
    user = User.query.get(user_id)
    event = Event.query.get(event_id)
    message = f"Reminder: {event.name} is due on {event.deadline}"
    status = send_email(user.email, f"Reminder: {event.name}", message)
    
    # Log notification
    log = NotificationLog(user_id=user.id, event_id=event.id, delivery_status=status)
    db.session.add(log)
    db.session.commit()
    print(f"Notification sent to {user.name}, status: {status}")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)
