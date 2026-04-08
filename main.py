# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.



import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
receiver_email = 'godstimemacaulay@gmail.com'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime
import random
import pandas
today_month = datetime.now().month
today_day = datetime.now().day

today = (today_month, today_day)



data  = pandas.read_csv('birthdays.csv')

birth_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birth_dict:
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
        letter = file.read()
        new_letter = letter.replace('[NAME]', birth_dict[today]['name'])




# Create the root message
msg = MIMEMultipart("alternative")
msg["Subject"] = "🚀 Happy Birthday!"
msg["From"] = MY_EMAIL
msg["To"] = receiver_email

# HTML content with inline CSS
html = f"""
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 10px;">
      <h2>{birth_dict[today]['name']}!</h2>
      <p>'{new_letter}'</p>
      <br>
      <p>Check out our cool image below:</p>
      <img src="https://images.unsplash.com/photo-1773332611628-9e1bdce4881b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxfHx8ZW58MHx8fHx8"
           alt="App Image" style="width:100%; border-radius: 10px;">
      <p><a href="https://lovable.dev/dashboard" style="background-color: #1a73e8; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px;">Get Started</a></p>
    </div>
  </body>
</html>
"""

# Attach HTML to the email
msg.attach(MIMEText(html, "html"))

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(MY_EMAIL, MY_PASSWORD)
    server.sendmail(MY_EMAIL, receiver_email, msg.as_string())

print("HTML email sent successfully!")



