import smtplib
import os
from config import Config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(recipient, filename):
    sender = Config.EMAIL_USER
    password = Config.EMAIL_PASS
    filepath = os.path.join(Config.PDF_FOLDER, filename)

    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = "Your Salary Slip"

        body = "Please find attached your salary slip."
        msg.attach(MIMEText(body, "plain"))

        attachment = open(filepath, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)
        attachment.close()

        server = smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(str(e))
        return False
