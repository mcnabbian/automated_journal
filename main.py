import smtplib, ssl
import getpass

port = 465 # For gmail SSL
password = getpass.getpass("Type your password and hit enter: ") # so the pass doesn't show up in my code

context = ssl.create_default_context() # something that helps establish ssl connection

with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
    server.login('mcnabbiantesting@gmail.com', password)
    # TODO: send email here