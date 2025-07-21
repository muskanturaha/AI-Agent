# slack_alert.py
import json
import requests

def send_slack_alert(webhook_url: str, alert: dict):
    text = (
        f"🚨 *Spike in Negative Sentiment*\n"
        f"{alert['neg_high']} high-urgency angry/sad messages in the last 5 mins "
        f"({alert['percent']}% of {alert['total']})."
    )
    requests.post(webhook_url, data=json.dumps({"text": text}))
