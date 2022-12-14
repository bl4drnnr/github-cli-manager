import json
import sys
import requests
import curses

BASE_URL = 'https://api.github.com'


def send_request(endpoint, additional_options, method, token, body=None, query=None, stdscr=None):
    try:

        for item, value in additional_options.items():
            endpoint = endpoint.replace(item, value)

        request_url = BASE_URL + endpoint

        if len(query) > 0:
            request_url += query

        if len(token) != 0:
            headers = {
                'Authorization': f'Bearer {token}',
                'Accept': 'application/vnd.github+json'
            }
        else:
            headers = {
                'Accept': 'application/vnd.github+json'
            }

        if stdscr:
            stdscr.addstr(f'\n\nSending {method} request to {request_url}\n', curses.color_pair(2))
        else:
            print(f'Sending {method} request to {request_url}')

        json_body = json.dumps(body)
        if method == 'GET':
            request = requests.get(request_url, headers=headers)
        elif method == 'POST':
            request = requests.post(request_url, headers=headers, data=json_body)
        elif method == 'DELETE':
            request = requests.delete(request_url, headers=headers, data=json_body)
        elif method == 'PUT':
            request = requests.put(request_url, headers=headers, data=json_body)
        else:
            request = requests.patch(request_url, headers=headers, data=json_body)

        request.raise_for_status()

        if request.status_code != 204:
            json_object = json.loads(request.text)
            json_formatted_str = json.dumps(json_object, indent=2)
            return json_formatted_str
    except requests.exceptions.RequestException as e:
        error_message = e.response.json()
        if stdscr:
            stdscr.addstr(f'{error_message["message"]}\n', curses.color_pair(3) | curses.A_BOLD)
        else:
            print(f'{error_message["message"]}')
        sys.exit()
