import requests
import curses

BASE_URL = 'https://api.github.com'


def send_request(stdscr, token, endpoint, additional_options):
    try:

        for item, value in additional_options.items():
            endpoint = endpoint.replace(item, value)

        request_url = BASE_URL + endpoint

        if len(token) != 0:
            headers = {
                'Authorization': f'Bearer {token}',
                'Accept': 'application/vnd.github+json'
            }
        else:
            headers = {
                'Accept': 'application/vnd.github+json'
            }

        stdscr.addstr(f'\n\nSending request to {request_url}\n', curses.color_pair(2))

        request = requests.get(request_url, headers=headers)
        request.raise_for_status()
        return request.content
    except requests.exceptions.HTTPError as e:
        stdscr.addstr(f'{str(e)}\n', curses.color_pair(3) | curses.A_BOLD)
        return
