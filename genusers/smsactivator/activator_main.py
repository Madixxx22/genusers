#from aiohttp import ClientSession
from requests import Session
#from smsactivate.api import SMSActivateAPI
from genusers.smsactivator.work_with_number import WorkNumber
from genusers.config import SMS_KEY


def activator_main() -> WorkNumber:
    #smsactivator = SMSActivateAPI(SMS_KEY)
    #smsactivator.debug_mode = True
    with Session() as session:
        current_number = WorkNumber(session)
        #current_number.buy_number()
    return current_number