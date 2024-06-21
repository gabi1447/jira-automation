from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

@app.route('/createjira', methods=['POST'])
def create_jira_ticket():
    url = os.getenv("URL")
    email = os.getenv("EMAIL")
    api_token = os.getenv("API_TOKEN")

    if request.is_json:
        data = request.get_json()
        issue_comment = data.get('comment', {}).get('body')
        title = data.get('issue', {}).get('title')
        description = data.get('issue', {}).get('body')

    auth = HTTPBasicAuth(email, api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
            "content": [
            {
            "content": [
                {
                    "text": title,
                    "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
            "id": "10000"
        },
        "project": {
            "key": "TES"
        },
        "summary": description,
        },
        "update": {}
    } )

    
    
    if issue_comment == "/jira":
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    else:
        return "Error"
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
