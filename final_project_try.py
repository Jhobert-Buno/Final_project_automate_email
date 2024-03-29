import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  # pip install python-dotenv

port = 587
email_server = "smtp.gmail.com"

# load the environment
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# read environment variables
sender_email = "jhobertbuno02valdez@gmail.com"
password_email = "gqzmamtmkqauubdc"

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Jhobert Buño", f"{sender_email}"))
    message["To"] = receiver_email
    message["BCC"] = sender_email

    message.set_content(
        f"""\
        Hi {name},
        I hope you are well. 
        I just wanted to drop you a quick note to remind you that {amount} pesos in respect of our invoice {invoice_no} is due for payment on {due_date}. 
        I would be really grateful if you could confirm that everything is on track for payment. 
        Best regards, 
        JHOBERT
        """
    )

    # Add the HTML version
    # container, with the original text message as the first part and the new HTML
    # message as the second part.
    message.add_alternative(
        f"""\
        <html>
          <body>
            <p>Hi {name},</p>
            <p>I hope you are well.</p>
            <p>I just wanted to drop you a quick note to remind you that <strong>{amount} pesos</strong> in respect of our invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
            <p>Best regards,</p>
            <p>JHOBERT</p>
          </body>
        </html>
        """,
        subtype="html"
    )

    with smtplib.SMTP(email_server, port) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Jhobert Buño",
        receiver_email="jobertbuno02@gmail.com",
        due_date="11, August 2023",
        invoice_no="INV-21-12-009",
        amount="5",
    )