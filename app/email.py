import smtplib
from flask_mail import Message
from app import mail,app
from flask import render_template
from threading import Thread

# def send_async_email(app, msg):
#     with app.app_context():
#         server = smtplib.SMTP('smtp.gmail.com')
#         server.starttls()
#         server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         server.sendmail(app.config['ADMINS'][0] , app.config['ADMINS'][1], msg)

def send_email(subject,sender,recipients,text_body,html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    server.sendmail(app.config['ADMINS'][0], recipients, msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        '[Flask Project] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',user=user,token=token),
        html_body=render_template('email/reset_password.html',user=user,token=token)
    )
