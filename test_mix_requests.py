import time
import requests
from concurrent.futures import ThreadPoolExecutor
import random
import string

def generate_random_email():
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    domain = random.choice(domains)
    return f"{username}@{domain}"

def send_request(endpoint, data=None, headers=None):
    try:
        post_response = requests.post(endpoint, json=data, headers=headers) if data else requests.get(endpoint)
        print(f"Status: {post_response.status_code}, Response: {post_response.json().get('message')}")
        get_response = requests.get(f"{endpoint}/{data['email']}", headers=headers)
        get_data = get_response.json()
        print(f"Status: {get_response.status_code}, Response {get_data.get('email')}, blocked: {get_data.get('blocked_reason')}, reason: {get_data.get('email')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def gradual_load_test(endpoint, start_rps, end_rps, duration, steps, headers=None):
    interval = duration / steps  # Duration for each RPS step

    for step in range(steps):
        rps = start_rps + step * (end_rps - start_rps) // steps
        print(f"Step {step} Sending {rps} post and get request per second...")
        with ThreadPoolExecutor(max_workers=rps) as executor:
            for _ in range(rps):
                random_email = generate_random_email()
                data = {"email": random_email,"app_uuid": "123e4567-e89b-12d3-a456-426614174000","blocked_reason": "Spamming"}  # Replace with payload for POST requests, if needed
                executor.submit(send_request, endpoint, data, headers)
                
        time.sleep(interval)  # Wait before increasing the load



# Usage
endpoint = "http://my-application-lb-1734885134.us-west-2.elb.amazonaws.com/blacklists"
start_rps = 1
end_rps = 1
duration = 6000  # Total duration in seconds
steps=6000
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.3J-lwqipiMTiRzWCEjuey3v-n7pjDTBV1FZBpHx6plI"}  # Replace with necessary headers, if any

gradual_load_test(endpoint, start_rps, end_rps, duration, steps, headers)