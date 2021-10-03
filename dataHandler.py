import requests
import datetime
from sgp4.api import Satrec, jday
from requests.models import HTTPError
from sgp4.model import Satellite


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


def process_data():
    with open('data.txt', 'rt') as file:
        lines = file.readlines()
        lines = '\n'.join([line.strip() for line in lines if line.strip() != ''])
        lines = lines.split('\n')

        # names = [line for line in lines[:: 3]]
        # row_1 = [line for line in lines[1::3]]
        # row_2 = [line for line in lines[2::3]]
        for i in range(0, len(lines), 3):
            name, row1, row2 = lines[i : i+3]

            satellite = Satrec.twoline2rv(row1, row2)
            jd, fr = jday(2021, 10, 3, 9, 56, 30)
            e, r, v = satellite.sgp4(jd, fr)
            print(e,r,v)


