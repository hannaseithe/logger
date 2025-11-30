import requests

def log(message):
    api_url = "http://localhost:8000/logs"
    level="info"
    log_json = {"message": message, "level": level}
    response = requests.post(api_url, json=log_json)
    print(response.status_code)