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
                'Authorization': f'Bearer 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',
                'Accept': 'application/vnd.github+json'
            }
        else:
            headers = {
                'Accept': 'application/vnd.github+json'
            }

        stdscr.addstr(f'\n\nSending request to {request_url}\n', curses.A_BOLD | curses.COLOR_GREEN)

        data = requests.get(request_url, headers=headers)
        return data.json()
    except Exception as e:
        raise Exception(e)
