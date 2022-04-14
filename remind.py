from twilio.rest import Client
import schedule
import time
import config


client = Client(config.account_sid, config.auth_token)

userName = input("Please enter your name here: ")
morningMeds = input("Please input your morning medications: ")
eveningMeds = input("Please input your evening medications: ")

helloMSG = "Hi "
morningMSG = "your morning meds are "
space = " "
nightMSG = "your evening meds are "

morningAnnouncement = helloMSG + userName + space + morningMSG + morningMeds
eveningAnnouncement = helloMSG + userName + space + nightMSG + eveningMeds


def send(x):

    call = client.messages.create(
        to=config.to,
        from_="+18607184148",
        body=morningAnnouncement
    )


schedule.every().day.at("08:00").do(send,'It is 08:00')


def send(y):

    call = client.messages.create(
        to="+17047737799",
        from_="+18607184148",
        body=eveningAnnouncement
    )


schedule.every().day.at("21:00").do(send,'It is 21:00')


while True:
    schedule.run_pending()
    time.sleep(60)
