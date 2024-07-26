#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import time
from flight_search import FlightSearch
import requests
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
print(sheet_data)
users_data = data_manager.get_customer_emails()
print(users_data)

#Para actualizar IATA CODE si es que hace falta en la hoja
# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#         time.sleep(2)
#         #print(f"sheet_data:\n {sheet_data}")
#
#         data_manager.destination_data = sheet_data
#         data_manager.update_destination_codes()

data_manager.users_data = users_data
user_emails_list = [row["whatIsYourEmail?"] for row in data_manager.users_data]
print(user_emails_list)

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")

for destination in sheet_data:
    flights = flight_search.get_flight_offer(destination["iataCode"], tomorrow, six_month_from_today, ORIGIN_CITY)
    if flights is None or not flights["data"]:
        print("Vuelo con escalas")
        flights = flight_search.get_flight_offer(destination["iataCode"], tomorrow, six_month_from_today, ORIGIN_CITY,
                                                 is_direct=False)
    cheapest_flight = flight_data.find_cheap_flights(flights)
    print(f"{destination["city"]}: ${cheapest_flight.price} with {cheapest_flight.stops} stops")
    #print(f"{cheapest_flight.destination_airport}: ${cheapest_flight.price} with {cheapest_flight.stops} stops")
    time.sleep(3)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        #SEND SMS - Personal
        notification_manager.send_notification(cheapest_flight.price, cheapest_flight.origin_airport,
                                               cheapest_flight.destination_airport, cheapest_flight.out_date,
                                               cheapest_flight.return_date, cheapest_flight.stops)
        #SEND EMAILS - For Users/Customers
        notification_manager.send_emails(cheapest_flight.price, cheapest_flight.origin_airport,
                                               cheapest_flight.destination_airport, cheapest_flight.out_date,
                                               cheapest_flight.return_date, user_emails_list, cheapest_flight.stops)


