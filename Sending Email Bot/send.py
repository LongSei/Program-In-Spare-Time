import sys
import requests
from datetime import datetime
from dotenv import load_dotenv
from formatting import format_msg
from send_mail import send_mail
import os

def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None
    msg = format_msg(my_name=name)
    try:
        send_mail(text=msg, to_emails= [to_email], html=None)
        report = """Status: {name} {to_email}: SENT""".format(name = name, to_email = to_email)
    except:
        report = """Status: {name} {to_email}: NOT_WORKING""".format(name = name, to_email = to_email)
    return report

if __name__ == "__main__":
    load_dotenv()
    name = []
    email = []
    path_name = os.getenv('path_name') # Direct to mail file
    path_mail = os.getenv('path_mail') # Direct to name file
    f = open(path_mail, "r")
    email = f.read().split(' ')
    f = open(path_name, "r")
    name = f.read().split(' ')
    for i in range(0, len(name)): 
        response = send(name[i], to_email=email[i], verbose=True)
        print(response)