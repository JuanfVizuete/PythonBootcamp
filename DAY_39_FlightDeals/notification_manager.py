from twilio.rest import Client
import os
from dotenv import load_dotenv

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    def send_notification(self, price, departure, arrival, out_date, inbound_date):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"-Low price alert! Only USD{price} to fly from {departure} to {arrival}, on {out_date} "
                 f"until {inbound_date}",
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),  # Twilio number
            to=os.getenv("TWILIO_TO_NUMBER"),  # Verified numbers in Twilio - destinatario
        )
        print(message.status)