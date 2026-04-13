import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


api_key = '461c99bac2f30da64d502a66fd80a5d1'
url = 'https://api.openweathermap.org/data/2.5/forecast'

params = {
    'lat': 4.824167,
    'lon': 7.033611,
    'cnt': 4,
    'appid': api_key,
}

response = requests.get(url, params=params)
conditions = response.json()['list']

is_rain = False

for w in conditions:
    weather_id = int(w['weather'][0]['id'])

    # Get time
    timestamp = w['dt']
    time = datetime.fromtimestamp(timestamp)
    timee = time.strftime("%I:%M %p")

    if weather_id < 700:
        is_rain = True
        print(f"Rain expected at {timee}")

if is_rain:

    # Your email details
    sender_email = "godstimemacaulay@gmail.com"
    receiver_email = "godstimemacaulay@gmail.com"
    password = "kbffdxzivkinwdcl"  # NOT your real password

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Rain Alert"

    body = f"Hello, rain expected at {timee}"
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure connection
    server.login(sender_email, password)

    # Send email
    server.send_message(msg)
    server.quit()


else:
    # Your email details
    sender_email = "godstimemacaulay@gmail.com"
    receiver_email = "godstimemacaulay@email.com"
    password = "kbffdxzivkinwdcl"  # NOT your real password

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Test Email"

    body = "Hello, this is a test email from Python, no rain today!"
    msg.attach(MIMEText(body, f"No rain expected today"))

    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure connection
    server.login(sender_email, password)

    # Send email
    server.send_message(msg)
    server.quit()


