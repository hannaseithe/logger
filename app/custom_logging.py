import requests

def log(*,message,level="info"):
    api_url = "http://localhost:8000/logs"
    log_json = {"message": message, "level": level}
    try:
        response = requests.post(api_url, json=log_json)
        print(f"Log Server returned: {response.status_code}")
    except:
        print("Exception occurred")
