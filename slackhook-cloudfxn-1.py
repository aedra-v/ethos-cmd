import requests


def coffee_time(request):
    headers = {
        'Content-Type': 'application/json'
    }
    
    request_json = request.get_json()
    url = "https://hooks.slack.com/services/TEAMID/CHANNEL/WEBHOOK"
    payload = '{"text":"It is the coffee time!"}'
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
