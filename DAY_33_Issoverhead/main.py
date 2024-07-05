import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -0.180653
MY_LONG = -78.467834
MY_EMAIL = "juanvizuetevallejo@gmail.com"
PASSWORD = "gbbimjzyubriiivq"


#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LAT - 5 <= iss_longitude <= MY_LAT + 5

def send_email(to_email, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # Securing connection
        connection.starttls()
        # Login
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send mail
        connection.sendmail(
            from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{body}"
            )

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
#
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look Up!")
        send_email("juanvizuete.python@yahoo.com", "Look Up!", "The ISS is close!")





