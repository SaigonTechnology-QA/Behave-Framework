import json
import requests
from resources.constant.constants import Contanst

class JsonHelper:
    global response

    def __init__(self) -> None:
        pass
    
    def method_call(self, method, endpoint) -> str:
        request_method = method.upper()
        end_point = endpoint.strip()

        if request_method == 'get':
            url = Contanst.BASEURL + end_point
            headers = ''
            response = requests.request("GET", url, headers=headers)
            return response

        if request_method == 'post':
            url = Contanst.BASEURL + end_point
            headers = ''
            payload = json.dumps()
            
            response = requests.request("POST", url, headers=headers, data=payload)
            return response
        

    def get_status_code(self) -> str:
        return response.status_code
    

        


