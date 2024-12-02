import time
import requests
from concurrent.futures import ThreadPoolExecutor
import random
import string
from datetime import datetime, timedelta

def generate_random_email():
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    domain = random.choice(domains)
    return f"{username}@{domain}"

def send_request(endpoint, data=None, headers=None):
    try:
        response = requests.post(endpoint, json=data, headers=headers) if data else requests.get(endpoint)
        print(f"Status: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def random_pause_load_test(endpoint, headers=None, duration_minutes=15):
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    print(f"Starting random pause load test for {duration_minutes} minutes...")

    while datetime.now() < end_time:
        random_email = generate_random_email()
        data = {
            "email": random_email,
            "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
            "blocked_reason": "Spamming"
        }
        send_request(endpoint, data, headers)
        pause_time = random.randint(1, 5)  # Random pause between 1 and 5 seconds
        print(f"Pausing for {pause_time} seconds...")
        time.sleep(pause_time)

# Usage
load_balancer_url = "http://my-application-lb-1975494205.us-west-2.elb.amazonaws.com"
endpoint = load_balancer_url+"/blacklists"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.3J-lwqipiMTiRzWCEjuey3v-n7pjDTBV1FZBpHx6plI"
}

# Run the random pause load test
print("Start")
random_pause_load_test(endpoint, headers=headers, duration_minutes=15)
