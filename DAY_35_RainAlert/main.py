import requests
import smtplib
import os

api_key = os.environ.get("OWM_API_KEY")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": -0.180653,
    "lon": -78.467834,
    "appid": api_key,
    "cnt": 4,
}

MY_EMAIL = "juanvizuetevallejo@gmail.com"
PASSWORD = os.environ.get("EMAIL_PWD")


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


response = requests.get(url=OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_list = weather_data["list"]

#weather_next_hours = [hour["weather"][0]["id"] for hour in weather_list]
will_rain = False
for hour in weather_list:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")
    send_email("juanvizuete.python@yahoo.com","IT'S GONNA RAIN TODAY!", "Bring an umbrella!")

