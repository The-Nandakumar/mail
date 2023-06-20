#Created at 10th March 2023
#Nandakumar
#Updated at 20th June 2023
#This script will ask your from address, to address and your password for outlook
import smtplib
from email.message import EmailMessage
import getpass

email = EmailMessage()
#Declaring all details in variables
from_address = input("[+] Enter your mail address: ")  #my mail address
to_address = input("[+] To address: ") #To address
subject = 'This is a subject'
content_of_the_mail = "Congratulation you received a mail"

email['from'] = from_address
email['to'] = to_address
email['subject'] = subject
email.set_content(content_of_the_mail)

server_name = "smtp.office365.com"
port_number = 587

with smtplib.SMTP(host=server_name, port=port_number) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(from_address, getpass.getpass("[+] Enter your email password:"))
    smtp.send_message(email)
print("Mail sent successfully")
