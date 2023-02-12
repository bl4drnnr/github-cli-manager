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

        proceed_with_pagination = False
        if len(query) > 0 and 'all=true' not in query:
            request_url += query
        if 'all=true' in query:
            proceed_with_pagination = True

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

        if not proceed_with_pagination:
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
        else:
            query = query[1:]
            query = query.replace('all=true', '')
            pagination_query = ''
            page = 1
            per_page = 100

            parsed_query = query.split('&')
            for q in parsed_query:
                if q.split('=')[0] not in ['per_page', 'page']:
                    pagination_query += f'&{q}'

            pagination_query = pagination_query[1:]
            pagination_query += f'{"&" if len(pagination_query) >= 0 else ""}per_page={per_page}&page='

            result = []

            request = requests.get(f'{request_url}?{pagination_query}{page}', headers=headers)
            request.raise_for_status()

            json_object = json.loads(request.text)
            json_formatted_str = json.dumps(json_object, indent=2)

            if stdscr is not None:
                stdscr.addstr(f'It will take some time. Press any key to continue.', curses.color_pair(4))
                stdscr.getch()
            else:
                print('It will take some time...')

            while json_formatted_str != '[]':
                request = requests.get(f'{request_url}?{pagination_query}{page}', headers=headers)
                request.raise_for_status()

                json_object = json.loads(request.text)
                json_formatted_str = json.dumps(json_object, indent=2)

                for item in json_object:
                    result.append(item)

                page += 1

            json_formatted_str = json.dumps(result, indent=2)
            return json_formatted_str
    except requests.exceptions.RequestException as e:
        error_message = e.response.json()
        if stdscr:
            stdscr.addstr(f'{error_message["message"]}\n', curses.color_pair(3) | curses.A_BOLD)
        else:
            print(f'{error_message["message"]}')
        sys.exit()
