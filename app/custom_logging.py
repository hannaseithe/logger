import requests

def log(message):
    api_url = "http://localhost:8000/logs"
    level="info"
    log_json = {"message": message, "level": level}
    try:
        response = requests.post(api_url, json=log_json)
        print(response.status_code)
    except:
        print("Exception occurred")
