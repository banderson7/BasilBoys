import requests
import time

from outletAuth import (
    email,
    password
)

token = None
headers = None
turnOnBody = None
turnOffBody = None
loginEndpoint = "https://smartapi.vesync.com/cloud/v1/user/login"
switchEndpoint = "https://smartapi.vesync.com/15a/v1/device/devicestatus"

def login():
    loginBody = {
        "email": email,
        "password": password,
        "acceptLanguage": "en",
        "appVersion": "2.5.1",
        "method":"login",
        "phoneBrand":"SM-N9005",
        "phoneOS": "Android",
        "timeZone": "UTC",
        "traceId": str(time.time()),
        "userType" :"1",
        "devToken":""
    }
    r = requests.post(loginEndpoint, json=loginBody, headers=None, timeout=5)
    print(r.json())
    loginResult = r.json()['result']
    token = loginResult['token']
    headers={
        'Content-Type':'application/json',
        'tk': token,
        'accountID': "",
        'accept-language':"en",
        'tz': "UTC",
        'appVersion':"2.5.1"
    }
login()
turnOnBody ={
    "token": token,
    "accountID": "1334313",
    "status": "on",
    "timeZone":"UTC",
    "uuid": "54c30446-b1c8-4da6-a347-a2b109c46bb8"
}

turnOffBody ={
    "token": token,
    "accountID": "1334313",
    "status": "off",
    "timeZone":"UTC",
    "uuid": "54c30446-b1c8-4da6-a347-a2b109c46bb8"
}
r = requests.put(switchEndpoint, json=turnOffBody , headers=headers, timeout=5)
print(r.json())