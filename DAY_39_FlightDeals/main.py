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
flight_data = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
#print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_cities_code(row["city"])
        time.sleep(2)

    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")

for destination in sheet_data:
    flights = flight_search.get_flight_offer(destination["iataCode"], tomorrow, six_month_from_today, ORIGIN_CITY)
    cheapest_flight = flight_data.find_cheap_flights(flights)
    print(f"{destination["city"]}: ${cheapest_flight.price}")
    time.sleep(2)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        notification_manager.send_notification(cheapest_flight.price, cheapest_flight.origin_airport,
                                               cheapest_flight.destination_airport, cheapest_flight.out_date,
                                               cheapest_flight.return_date)


