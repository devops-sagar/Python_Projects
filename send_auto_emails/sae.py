# 

import os
import random
import smtplib

def auto_emails():
    user = input("Please Enter your Name: ")
    email = input(f"Hello {user}! Please Enter your Email ID: ")
    message = (f"Dear {user}, Thanks for getting connected with Me!")

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login("@gmail.com", "")
    s.sendmail('&&&&&&&&&&&&', email, message)
    print("Email sent successfully...!")

auto_emails()