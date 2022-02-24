from twilio.rest import Client
import schedule
import time
import config

SID = config.account_sid
token = config.auth_token

client = Client(SID, token)

def send(t):

    call = client.messages.create(
        config.to,
        from_= "+18607184148",
        body="Hi Madi! Don't forget your medications tonight."
    )

schedule.every().day.at("22:00").do(send,'It is 22:00')

while True:
    schedule.run_pending()
    time.sleep(60)