import requests 
import datetime

TOKEN = "gqXYDBey%@vnBktJ"
pix_endpoint = "https://pixe.la/v1/users"

user_params = { 
    "token": TOKEN,
    "username": "niki",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url= pix_endpoint, json= user_params)
# print(response.text)

graph_url = f"{pix_endpoint}/niki/graphs"

graph_config = { 
    "id": "testgraph1",
    "name": "Commit Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}

headers = {
    
    "X-USER-TOKEN":	TOKEN
}

# response = requests.post(url= graph_url, json= graph_config, headers= headers)
# print(response.text)

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_url}/testgraph1" 
pixel_config = {
    "date": date,
    "quantity": "15",
    
}

response = requests.post(url= post_pixel_endpoint, json= pixel_config, headers= headers)
print(response.text)

# reponse = requests.delete(url= post_pixel_endpoint, headers= headers)
# print(reponse.text)



