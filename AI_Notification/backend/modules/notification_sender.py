import smtplib
from email.mime.text import MIMEText
from backend.config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(to_email, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        return "Sent"
    except Exception as e:
        print("Error sending email:", e)
        return "Failed"
