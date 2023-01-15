"""
- Automate Teams with your first Python Alerting Bot:

Tutorial: https://medium.com/towards-data-science/automate-teams-with-your-first-python-alerting-bot-bcc8f7c6ee5a
https://apps.timwhitlock.info/emoji/tables/unicode
Color Hex Color Codes: https://www.color-hex.com
"""

def get_connector_mesa_teams():
    """
      - URL responsible for the connection with the channel (Economia > Reminders) in Teams
        via 'Incoming Webhook' connector through Tenax Econ Bot.
    """
    return 'https://tnaxcapital.webhook.office.com/webhookb2/2aebf027-161f-448d-826a-9478d0b7c1b9@cc2d437c-9657-43ce-b9b9-a84614e5f413/IncomingWebhook/3b7101a778a2404286f607d5b70ca34a/e6e9dbe7-7777-463e-8c2c-7a88b429d5e9'

import requests

def send_teams_message(webhook_url:str, content:str, title:str, color:str="000000") -> int:
    """
      - Send a teams notification to the desired webhook_url
      - Returns the status code of the HTTP request
        - webhook_url : the url you got from the teams webhook configuration
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=webhook_url,
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