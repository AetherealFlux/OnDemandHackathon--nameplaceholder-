import requests

url = "https://api.on-demand.io/chat/v1/sessions"

payload = { "externalUserId": "1"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "apikey": "rdTbeG8dvFQcgtYL8r4SRowGVClreNFr"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
session_id = response.json()["data"]["id"]
print(session_id)

url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id

payload = {
    "responseMode": "sync",
    "endpointId": "predefined-openai-gpt4o",
    "query": "What's the air quality in Oxford, UK today?",
    "pluginIds": ["plugin-1726246679"]
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "apikey": "rdTbeG8dvFQcgtYL8r4SRowGVClreNFr"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)