import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


EMAIL_PASS = "ugcycdggwufxwjim"
EMAIL_USER = "11c.tohaneanu@gmail.com"
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_SERVER_PORT = 465 # post smtp pentru conexiuni securizate

message = MIMEMultipart("alternative")
message["Subject"] = "HTML Test"
message["From"] = EMAIL_USER
message["To"] = EMAIL_USER

html = """\
<html>
  <body>
    <h2>Hello, from my py code</h2>
    <p2>Hello from my code. This email is sent from a <n>Python</b> script.</p>   
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

server = smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_SERVER_PORT)
server.login(EMAIL_USER, EMAIL_PASS)
server.sendmail(
    EMAIL_USER,
    EMAIL_USER,
    message.as_string()
)


