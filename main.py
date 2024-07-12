import smtplib
from flask import Flask
from config import getConfig

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    status = send_email()
    return f'<h1>{status}</h1>'

def send_email():
    FROM = getConfig("from_email")
    TO = getConfig("to_email")
    SUBJECT = "Sending Email"
    TEXT = "I have sent this because I can't get through to you"
    PWD = getConfig("pwd")

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, PWD)
        server.sendmail(FROM, TO, message)
        server.close()
        return "Successful"
    except:
        return "Failure"
