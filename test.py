import requests

url = "https://api.on-demand.io/chat/v1/sessions"

payload = { "externalUserId": "1"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "apikey": "WQXfBI84GSMLt8fXMgvz16wLE5TjPBoN"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
session_id = response.json()["data"]["id"]
print(session_id)

url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id

payload = {
    "responseMode": "sync",
    "endpointId": "predefined-openai-gpt4o",
    "query": "Give me a todo list of habit cultivation plan for today. The habit is reading book and the plan is read two hours everyday",
    "pluginIds": ["plugin-1731202033"]
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "apikey": "WQXfBI84GSMLt8fXMgvz16wLE5TjPBoN"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)