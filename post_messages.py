"""
Author: Victor Gimenes
Date: 08/05/2022

Módulo criado para automatizar menssagens de alertas em canais do Teams. 

Tutorial:               https://medium.com/towards-data-science/automate-teams-with-your-first-python-alerting-bot-bcc8f7c6ee5a
Emojis:                 https://apps.timwhitlock.info/emoji/tables/unicode
Color Hex Color Codes:  https://www.color-hex.com
"""

def get_connector():
    """
      - URL responsible for the connection with the channel in Teams
        via 'Incoming Webhook' connector through Bot.
    """
    return 'enter the webhook url you got from the teams webhook configuration here!'

import requests

def send_teams_message(content:str, title:str, color:str="000000") -> int:
    """
      - Send a teams notification to the desired webhook url
      - Returns the status code of the HTTP request
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=get_connector(),
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": color,
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "activitySubtitle": content
            }],
        },
    )
    return response.status_code # Should be 200
