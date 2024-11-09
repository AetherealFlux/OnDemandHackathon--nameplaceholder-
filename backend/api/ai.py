import requests

class OnDemand():
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        # "apikey": "rdTbeG8dvFQcgtYL8r4SRowGVClreNFr"
        "apiKey": "WQXfBI84GSMLt8fXMgvz16wLE5TjPBoN"
    }
    payload = {
        "responseMode": "sync",
        "endpointId": "predefined-openai-gpt4o"
    }
    def __create_chat_session(self) -> str:
        payload = { "externalUserId": "1"}
        response = requests.post("https://api.on-demand.io/chat/v1/sessions", json=payload, headers=self.headers)
        session_id = response.json()["data"]["id"]
        return session_id

    def genSubtodos(self, todo: str) -> str:
        session_id = self.__create_chat_session()
        url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id
        query = "Give me a todo list of subtasks of a task. The task is %s. Also give the expected duration for each subtasks. The expected duration should in days if it is long or minute if it is short. Give the answer in json with \"response\":\"Success\", \"content\": collect of tasks in json with keys \"title\" and \"estimatedDuration\" and \"units\" of \"day\" or \"minute\". estimatedDuration is 0 if you feel it is instant to complete. If the task or comment is confusing, give me json with \"response\":\"error\"\""%(todo)
        self.payload["query"] = query
        self.payload["pluginIds"] = ["plugin-1731192572"]
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json()["data"]["answer"][7:-3]
    
    def genHabitTodo() -> str:
        ...
    
    def genSchedule() -> str:
        ...
    
    def genSummary() -> str:
        ...

Gen = OnDemand()
print(Gen.genSubtodos("Play Football"))