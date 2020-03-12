import smtplib, ssl
import getpass

sender = input("Type the gmail address you'd like to send from: ")
password = getpass.getpass("Type your password and hit enter: ")  # so pass doesn't show up in code
receiver = input("Type the gmail address you'd like to receive the email: ")

message = """\
Subject: TEST SUBJECT

This is an automated message!"""

port = 465 # For gmail SSL
context = ssl.create_default_context() # something that helps establish ssl connection

with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Successfully sent email!")
    except smtplib.SMTPAuthenticationError as e:
        print("Invalid login. Username or Password incorrect.")
