import requests


def slackhook_event(request):
    headers = {
        'Content-Type': 'application/json'
    }
    
    request_json = request.get_json()
#    url = "https://hooks.slack.com/services/TEAMID/CHANNEL/WEBHOOK" ##### need to specify #
    payload = '{"text":"It is the coffee time!"}'
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    
def slackhook_rawimport(request):
    headers = {
        'Content-Type': 'application/json'
    }
    
    request_json = request.get_json()
#    url = "https://hooks.slack.com/services/TEAMID/CHANNEL/WEBHOOK" ##### need to specify #
    payload = '{"text":"It is the coffee time!"}'
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    
def slackhook_dataparse(request):
    headers = {
        'Content-Type': 'application/json'
    }
    
    request_json = request.get_json()
#    url = "https://hooks.slack.com/services/TEAMID/CHANNEL/WEBHOOK" ##### need to specify #
    payload = '{"text":"It is the coffee time!"}'
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
