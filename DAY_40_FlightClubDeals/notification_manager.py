from twilio.rest import Client
import os
import smtplib
from dotenv import load_dotenv

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.my_email = os.getenv("SMTP_EMAIL")
        self.my_password = os.getenv("SMTP_PASSWORD")

    def send_notification(self, price, departure, arrival, out_date, inbound_date, stops):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"-Low price alert! Only USD{price} to fly from {departure} to {arrival} with {stops} stops, on {out_date} "
                 f"until {inbound_date}",
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),  # Twilio number
            to=os.getenv("TWILIO_TO_NUMBER"),  # Verified numbers in Twilio - destinatario
        )
        print(message.status)

    def send_emails(self,price, departure, arrival, out_date, inbound_date, emails_list, stops):
        for email in emails_list:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                # Securing connection
                connection.starttls()
                # Login
                connection.login(user=self.my_email, password=self.my_password)
                # Send mail
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:Low price alert!\n\nOnly USD{price} to fly from {departure} to {arrival} with {stops}"
                        f" stops, on {out_date} until {inbound_date}"
                )