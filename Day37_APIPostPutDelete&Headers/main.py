import requests
import datetime as dt

USERNAME = "citizen-xx"
TOKEN = "bababooey"

YESTERDAY = dt.datetime(year=2025, month=5, day=14).strftime("%Y%m%d")
TODAY = dt.datetime.today().strftime('%Y%m%d')
print(YESTERDAY)

user_url = "https://pixe.la/v1/users"
graph_url = f"{user_url}/{USERNAME}/graphs"
pixel_url = f"{graph_url}/graph1"
update_url = f"{pixel_url}/{TODAY}"
delete_url = f"{pixel_url}/{YESTERDAY}"

# account_params = {
#     "token": USERNAME,
#     "username": TOKEN,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=user_url, params=account_params)
# response.raise_for_status()
# print(response.text)

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

# headers_dict = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(
#     url=graph_url, json=graph_config, headers=headers_dict)
# response.raise_for_status()
# print(response.text)

# pixel_config = {
#     "date": YESTERDAY,
#     "quantity": "7"
# }

# pixel_header = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(
#     url=pixel_url, json=pixel_config, headers=pixel_header)
# response.raise_for_status()
# print(response.text)

# update_config = {
#     "quantity": "7"
# }

# update_headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.put(
#     url=update_url, json=update_config, headers=update_headers)
# response.raise_for_status()
# print(response.text)

# delete_headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.delete(url=delete_url, headers=delete_headers)
# response.raise_for_status()
# print(response.text)
