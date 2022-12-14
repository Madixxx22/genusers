#import json
#import aiohttp
import requests
#from smsactivate.api import SMSActivateAPI
from genusers.config import SMS_KEY

class WorkNumber():
    params_count = {"api_key": SMS_KEY, "action": "getNumbersStatus",
                    "country": 0, "operator": "beeline"}
    params_buy = {"api_key": SMS_KEY, "action" : "getNumber",
                  "service": "ft", "operator": "beeline",
                  "country": 0}
    number = {}


    def __init__(self, session: requests.Session):
        self.url = "https://api.sms-activate.org/stubs/handler_api.php"
        self.session = session


    def status(self):
        with self.session.get(self.url, params=self.params_count) as response:
            count_bett_number = response.json()['ft_0']
    
        return count_bett_number

    def buy_number(self):
        with self.session.get(self.url, params=self.params_count) as response:
            count_bett_number = response.json()['ft_0']
        min_count_number = 30
        if count_bett_number > min_count_number:
            with self.session.get(self.url, self.params_buy) as response:
                self.number = response.json()

