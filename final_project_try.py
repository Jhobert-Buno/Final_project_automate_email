# import the needed modules
import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv #pip install python-dotenv

port = 587
email_server = "smtp.gmail.com"

#load the environment
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

#read environment variables
sender_email = os.getenv("email")
password_email = os.getenv("password")

def sender_email(subject, reciever_email, name, due_date, invoice_no, amount):
    #Create the base text message
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Jhobert Buño", f"{sender_email}"))
    message["To"] = reciever_email
    message["BCC"] = sender_email

    message.set_content(
        f"""\
        Hi {name},
        I hope you are well. 
        I just wanted to drop you a quick note to remind you that {amount} pesos in respect of our invoice {invoice_no} is due for payment on {due_date}. 
        I would be really grateful if you could confirm that everything is on track for payment. 
        Best regards 
        JHOBERT
        """
    )
    
































