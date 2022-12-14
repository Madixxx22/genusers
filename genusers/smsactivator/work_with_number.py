#import json
#import aiohttp
import requests
#from smsactivate.api import SMSActivateAPI
from genusers.config import SMS_KEY

class WorkNumber():
    number = {}


    def __init__(self, session: requests.Session):
        self.url = "https://api.sms-activate.org/stubs/handler_api.php"
        self.session = session


    def buy_number(self):
        params_count = {"api_key": SMS_KEY, "action": "getNumbersStatus",
                        "country": 0, "operator": "beeline"}
        params_buy = {"api_key": SMS_KEY, "action" : "getNumber",
                      "service": "ft", "operator": "beeline",
                      "country": 0}
        with self.session.get(self.url, params=params_count) as response:
            count_bett_number = response.json()['ft_0']
        min_count_number = 30
        try:
            if count_bett_number > min_count_number:
                with self.session.get(self.url, params_buy) as response:
                    self.number = response.json()
                    if "phoneNumber" not in self.number:
                        raise Exception("Error buy phone")
            else:
                raise Exception("Numbers on the service are less than 30")
        except:
            print("Error when buying a number!")
            print(self.number["message"])
            raise


    def get_activate_code(self):
        params_code = {"ip_key": SMS_KEY, "action" : "getStatus",
                       "id": self.number["activationId"]}
        params_change_status = {"ip_key": SMS_KEY, "action" : "setStatus",
                                "id": self.number["activationId"], "status": 3}
        with self.session.get(self.url, params=params_code) as response:
            try:
                activate_code = response.json()
                if "STATUS_OK" in activate_code:
                    with self.session.get(self.url, params=params_change_status) as res:
                        status = res.json()
                        if "ACCESS_RETRY_GET" not in status:
                            raise Exception("Error Status!")
                    return ("STATUS_OK", activate_code["STATUS_OK"])
                elif "STATUS_WAIT_CODE" in activate_code:
                    return ("STATUS_WAIT_CODE", activate_code)
                else:
                    raise Exception("Error activate_code")  
            except:
                print("Error when get status activate code!")
                print(activate_code["message"])
                raise

    def close_activate_code(self):
        params_change_status = {"ip_key": SMS_KEY, "action" : "setStatus",
                                "id": self.number["activationId"], "status": 6}
        try:
            with self.session.get(self.url, params=params_change_status) as response:
                status = response.json()
                if "ACCESS_ACTIVATION" not in status:
                    raise Exception("Error close status activate code")
                return status
        except:
            print("Error when close activate code!")
            print(status["message"])
            raise
