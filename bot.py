# Pulse-Daily Summary Bot
# Fetches-Weather(wttr.in)+a quote(zenquotes.io)
# Runs at 8AM IST using GitHub Actions
import requests
from datetime import date
def get_weather(city="Thiruvananthapuram"):
  '''fetches today's weather as a one line text summary'''
  url=f"https://wttr.in/{city}?format=3"
  try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    return response.text.strip()
  except Exception as e:
    return f"Weather unavailable({e})"
def get_quote():
  '''Fetch random motivational quotes from ZenQuotes'''
  url="https://zenquotes.io/api/random"
  try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    data=response.json()
    quote=data[0]["q"]
    author=data[0]["a"]
    return f'"{quote}"-{author}'
  except Exception as e:
    return f"Quote unavailable({e})"
def build_summary():
  '''assemble full daily summary for all data sources'''
  today=date.today().strftime("%A,%d %B %Y")
  weather=get_weather()
  quote=get_quote()
  summary=f"""
  ======================================
  PULSE- Daily Summary
  {today}
  ======================================
  Weather:
  {weather}
  Today's Quote:
  {quote}
  ======================================
  """
  return summary

import smtplib
import os
from email.mime.text import MIMEText

def send_email(summary):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASSWORD"]
    recipient = os.environ["EMAIL_TO"]

    msg = MIMEText(summary)
    msg["Subject"] = "Pulse Daily Summary"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg) 
    print("Email Sent Successfully!")

def run():
  '''Main entry point- run by GitHub Actions'''
  summary=build_summary()
  print(summary)
  send_email(summary)
  with open("daily_summary.txt","w",encoding="utf-8") as f:
    f.write(summary)
    print("Pulse ran successfully")
if __name__=="__main__":
  run()
  
