# Import Python packages
import smtplib
import os

# Set global variables
gmail_user = "ywamconvergetesting@gmail.com"
gmail_password = "converge7&"

# Create email contents
mail_from = gmail_user
mail_to = "xcalibur220@gmail.com"
mail_subject = "YWAM Converge Monthly Testing Results"
mail_msg_body = os.popen(
    "pipenv run pytest --timeout=60 --timeout_method=thread --env=dev -n=5 --dist=loadscope --max-worker-restart=0 -v"
).read()
mail_msg = f"""\
From: {mail_from}
To: {mail_to}
Subject: {mail_subject}
{mail_msg_body}
"""

# Send email
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(gmail_user, gmail_password)
server.sendmail(mail_from, mail_to, mail_msg)
server.close()
