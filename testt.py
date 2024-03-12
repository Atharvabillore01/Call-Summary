import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

def sending_email(result, email,file):
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')
    receiver_email = email
    subject = "Test Email"
    body = result

    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    audio_file = file
    with open(audio_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {audio_file}")
    message.attach(part)

    server = smtplib.SMTP_SSL("mail.parvatiavenue.in", 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASS)
    server.sendmail(EMAIL_ADDRESS, receiver_email, message.as_string())
    server.quit()

    print("Email sent successfully!")
