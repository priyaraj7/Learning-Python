# # Python Code Challenge #8: Send an Email

# Your goal is to implement a function, `send_email()`, that takes three input arguments for the recipient’s email address, the email’s subject line, and the email message body.

# ## Example Test Output
# ```console
# >>> send_email('recipient@email.com', ‘Notification', 'Everything is awesome!')
# ```

# The recipient should receive an email with the subject "Notification" and the message body "Everything is aweseome!"


import smtplib # Simple Mail Transfer Protocol

SENDER_EMAIL = 'YOUR_EMAIL@EMAIL.COM'  # replace with your email address
SENDER_PASSWORD = 'YOUR_PASSWORD'  # replace with your email password

def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)



# if __name__ == '__main__':
#     # replace receiver email address
#     send_email('RECEIVER@EMAIL.COM', 'Notification', 'Everything is awesome!')