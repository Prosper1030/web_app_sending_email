import smtplib, ssl

host = "smtp.gmail.com"
port = 465
username = "1030railgunjudeglight@gmail.com"
password = "ddmnhkmpbufsqgfo"
receiver = "1030railgunjudeglight@gmail.com"

message ="""\
Subject: test
hello
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)