import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/feae7d6e1ca0d95a510ab1ead27509b9/flightDeals/prices"
SHEET_HEADERS = {
    "Authorization": "Bearer waltzes-bent-curtanas-opsoniums"
}
SHEET_USERS_ENDPOINT = "https://api.sheety.co/feae7d6e1ca0d95a510ab1ead27509b9/flightDeals/users"


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data, headers=SHEET_HEADERS)

            print(response.text)

    def get_customer_emails(self):
        customer_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
