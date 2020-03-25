import smtplib, ssl
import getpass
from email.message import EmailMessage

# sender = input("Type the gmail address you'd like to send from: ")
password = getpass.getpass("Type your password and hit enter: ")  # so pass doesn't show up in code
# receiver = input("Type the gmail address you'd like to receive the email: ")

msg = EmailMessage()
msg['To'] = 'mcnabbiantesting@gmail.com'
msg['From'] = 'mcnabbiantesting@gmail.com'
msg['Subject'] = 'FOO SUBJECT'

# plain-text message body contents
msg.set_content('blah blah blah')

# Add the html version.  This converts the message into a multipart/alternative
# container, with the original text message as the first part and the new html
# message as the second part.
# Uses plain-text in event that recipient has HTML messages off
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

port = 465  # For gmail SSL
context = ssl.create_default_context()  # something that helps establish ssl connection

with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
    try:
        server.login('mcnabbiantesting@gmail.com', password)
        server.send_message(msg)
        print("Successfully sent email!")
    except smtplib.SMTPAuthenticationError as e:
        print("Invalid login. Username or Password incorrect.")
