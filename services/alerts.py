import http.client, urllib
from functools import lru_cache
from configs.env_config import env_settings

'''
Sends notifications through Pushover API
https://github.com/tiangolo/fastapi/issues/2336#issuecomment-739510310
'''

def pushDeviceAlert(new_alert_message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": env_settings.pushover_api_token,
        "user": env_settings.pushover_user_key,
        "message": new_alert_message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    return   conn.getresponse()