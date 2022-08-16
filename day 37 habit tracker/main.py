import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "terminhnator1003"
TOKEN = "squashers-succoured-ehs-heist"
GRAPH_ID = "graph1"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# ---------- Creating a graph ---------- #

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Minutes of coding per day",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------- Drawing a pixel ------------ #

graph1_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many minutes did you code today?")
}

response = requests.post(url=graph1_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# ---------- Updating a pixel ---------- #

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# update_pixel_config = {
#     "quantity": "85"
# }

# response = requests.put(url=f"{update_endpoint}", json=update_pixel_config, headers=headers)
# print(response.text)

# ---------- Delete a pixel ---------- #

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220218"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response)
