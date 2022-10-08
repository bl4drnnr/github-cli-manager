import requests

BASE_URL = 'https://api.github.com'


def send_request(endpoint, additional_options, method, token, body=None):
    try:
        pass
    except requests.exceptions.RequestException as e:
        error_message = e.response.json()
        print(f'{error_message}')
        return
