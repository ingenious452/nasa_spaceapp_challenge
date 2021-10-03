import requests
from requests.models import HTTPError


def request_data(base_url, format_):
    query = {'NAME': 'DEB', 'FORMAT': format_}

    try:
        response =  requests.get(url, params=query)
    except TimeoutError as e:
        print(e)
    except ConnectionError as e:
        print(e)
    else:
        if response.ok:
            with open('data.txt', 'wt') as file:
                file.write(response.text)
        print('Done.')


url = 'https://celestrak.com//NORAD/elements/gp.php'

# request_data(url, '3LE')

with open('data.txt', 'rt') as file:
    lines = file.readlines()
    print(lines)