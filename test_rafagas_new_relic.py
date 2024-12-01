import time
import requests
from concurrent.futures import ThreadPoolExecutor
import random
import string

def generate_random_email():
    """Genera un email aleatorio para pruebas."""
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domains = ['test.com', 'email.com', 'demo.org', 'app.net']
    domain = random.choice(domains)
    return f"{username}@{domain}"

def send_request(endpoint, method="POST", data=None, headers=None):
    try:
        if method == "POST":
            response = requests.post(endpoint, json=data, headers=headers)
        elif method == "GET":
            response = requests.get(endpoint, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")
        print(f"Endpoint: {endpoint}, Method: {method}, Status: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def burst_load_test_with_random_requests(endpoints, rps, burst_duration, pause_duration, headers=None):
    """
    Envía ráfagas de solicitudes con aleatoriedad en endpoints y métodos, con pausas entre ráfagas.

    :param endpoints: Lista de endpoints y métodos [(endpoint, method)].
    :param rps: Cantidad de solicitudes por segundo.
    :param burst_duration: Duración total de la prueba en segundos.
    :param pause_duration: Tiempo en segundos entre ráfagas.
    """
    print(f"Starting burst load test with random endpoints and {rps} RPS for {burst_duration}s with pauses...")
    total_time = 0  # Tiempo total transcurrido
    with ThreadPoolExecutor(max_workers=rps) as executor:
        while total_time < burst_duration:
            start_time = time.time()

            # Enviar las solicitudes de la ráfaga
            for _ in range(rps):
                endpoint, method = random.choice(endpoints)
                if method == "POST":
                    random_email = generate_random_email()
                    data = {
                        "email": random_email,
                        "app_uuid": "burst-load-uuid",
                        "blocked_reason": "Testing burst load with random requests"
                    }
                    executor.submit(send_request, endpoint, method, data, headers)
                elif method == "GET":
                    random_email = generate_random_email()
                    executor.submit(send_request, f"{endpoint}/{random_email}", method, None, headers)

            elapsed_time = time.time() - start_time
            remaining_pause = max(0, pause_duration - elapsed_time)
            time.sleep(remaining_pause)

            total_time += pause_duration

endpoints = [
    ("http://my-application-lb-1189893953.us-east-1.elb.amazonaws.com/blacklists", "POST"),
    ("http://my-application-lb-1189893953.us-east-1.elb.amazonaws.com/blacklists", "GET")
]

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.3J-lwqipiMTiRzWCEjuey3v-n7pjDTBV1FZBpHx6plI"
}
rps = 50  # Solicitudes por segundo
burst_duration = 600  # Duración total de la prueba (en segundos)
pause_duration = 5  # Pausa entre ráfagas (en segundos)

burst_load_test_with_random_requests(endpoints, rps, burst_duration, pause_duration, headers)
