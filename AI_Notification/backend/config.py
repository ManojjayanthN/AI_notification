# Configurations for the backend
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "notification_system.db")

# Admin credentials
ADMIN_USERNAME = "manu"
ADMIN_PASSWORD = "1234"

# Email credentials for sending notifications
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_app_password"

# SMS credentials (Twilio example)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
