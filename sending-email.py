import smtplib
import ssl
from email.message import EmailMessage
import os
import sys

def send_email(subject, body, sender_email, receiver_email, password):
    """
    Sends an email from the sender to the receiver.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    sender_email (str): The sender's email address.
    receiver_email (str): The receiver's email address.
    password (str): The password for the sender's email account.
    """
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to set up and send an email.
    """
    subject = "Email From Assistant"
    body = "This is a test email from Robot!"

    sender_email = "virtualstudent.x@gmail.com"
    receiver_email = "mohamedkhaliljelassi00@gmail.com"

    # Fetching the password from an environment variable for security.
    password = os.getenv("EMAIL_PASSWORD")

    if not password:
        print("No password provided. Please set the EMAIL_PASSWORD environment variable.")
        sys.exit(1)

    send_email(subject, body, sender_email, receiver_email, password)

if __name__ == "__main__":
    main()

