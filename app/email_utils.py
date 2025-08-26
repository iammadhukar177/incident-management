from flask_mail import Message
from . import mail
from flask import current_app

def send_email(subject, body):
    msg = Message(subject, recipients=['admin@example.com'], body=body, sender=current_app.config['MAIL_USERNAME'])
    mail.send(msg)
