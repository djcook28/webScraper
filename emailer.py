import smtplib
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    PASSWORD = os.getenv("pythonGmailPass")
    SENDER = os.getenv("GMAIL")

    RECEIVER = SENDER

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECEIVER, message)