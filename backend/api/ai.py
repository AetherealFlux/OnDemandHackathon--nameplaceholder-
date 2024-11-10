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
        query = "Give me a todo list of subtasks of a task. The task is %s."%(todo)
        self.payload["query"] = query
        self.payload["pluginIds"] = ["plugin-1731192572"]
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json()["data"]["answer"][7:-3]
    
    def genHabitTodo(self,habit:str,plan:str) -> str:
        session_id = self.__create_chat_session()
        url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id
        query = "Give me a todo list of habit cultivation plan for today. The habit is %s and the plan is %s."%(habit,plan)
        self.payload["query"] = query
        self.payload["pluginIds"] = ["plugin-1731202033"]
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json()["data"]["answer"][7:-3]
    
    def genSchedule(self,data:str) -> str: #data:json string {"comment":{...},"tasks":[{...},{...}...]}
        session_id = self.__create_chat_session()
        url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id
        query = "Give me a one-day schedule for tasks %s."%(data)
        self.payload["query"] = query
        self.payload["pluginIds"] = ["plugin-1731195963"]
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json()["data"]["answer"][7:-3]
    
    def genSummary(self,data:str) -> str: #data:json string {"task":{...}} or {"schedule":{...}}
        session_id = self.__create_chat_session()
        url = "https://api.on-demand.io/chat/v1/sessions/%s/query" % session_id
        query = "Give me a summary of task or schedule. Input data is here %s"%(data) 
        self.payload["query"] = query
        self.payload["pluginIds"] = ["plugin-1731197745"]
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json()["data"]["answer"][7:-3]

Gen = OnDemand()
print(Gen.genSubtodos("Play Football"))