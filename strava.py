import time
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

AUTH_URL = "https://www.strava.com/oauth/token"


def get_auth():
    payload = {
        'client_id': os.environ.get("STRAVA_CLIENT_ID"),
        'client_secret': os.environ.get("STRAVA_CLIENT_SECRET"),
        'refresh_token': os.environ.get("STRAVA_REFRESH_TOKEN"),
        'code': os.environ.get("STRAVA_CLIENT_CODE"),
        'grant_type': "authorization_code"
    }

    response = requests.post(AUTH_URL, data=payload)
    #Save json response as a variable
    strava_tokens = response.json()
    # Save tokens to file
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(strava_tokens, outfile)
    return response.json()



if __name__ == "__main__":
    get_auth()