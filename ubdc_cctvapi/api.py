import json
import re
import html
import sys
from typing import Optional

import requests

LOCATIONS = ['Argyle_St_@_Brown_St', 'Argyle_St_@_Jamaica_St', 'Argyle_St_@_Oswald_St', 'Argyle_St_@_Oswald_St(static)',
             'Bellahouston_Park', 'Bellahouston_Park_pathway_near_PRW_gate', 'Broomielaw_@_James_Watt_St_(cam1)',
             'Broomielaw_@_James_Watt_St_(cam2)', 'Broomielaw_@_Washington_St', 'Broomielaw_Rear_of_Casino',
             'Byres_Rd_@_Dowanside_St', 'Clyde_Walkway_@_Dixon_St', 'Clyde_Walkway_@_Jamaica_St',
             'Clyde_Walkway_@_Stockwell_St', 'Clyde_walkway_@_McAlpine', 'Duke_St_@_Bellgrove',
             'Finnieston_Bridge_@_Lancefield_Quay', 'Gallowgate_@_High_St(cam1)', 'Gallowgate_@_High_St(cam2)',
             'George_Sq_@_South_Hanover_St', 'Glasgow_Green_Circles', 'Glasgow_Green_Doulton_Fountain',
             'Glasgow_Green_Path', 'Glasgow_Green_monument', 'Glasgow_Green_suspension_walkway',
             'Gordon_St_@_Renfield_St', 'High_St_@_George_St', 'Hope_St_@_Gordon_Street', 'Hope_St_@_Waterloo_St',
             'Kelvingrove_Park_Kelvin_Way', 'Kelvingrove_Park_entrance', 'Kelvingrove_Park_fountain',
             'Kelvingrove_Park_overview', 'Killermont_St_@_Royal_Concert_Hall', 'Maryhill_Forth_Clyde_Canal',
             'Maryhill_Rd_@_Shakespeare_St', 'Sauchiehall_St_@_Pitt_St', 'Tollcross_Park(cam1)', 'Tollcross_Park(cam2)',
             'Victoria_Rd_@_Allison_St']


def _extract_payload(text: str):
    pattern = re.compile(r'<p>(?P<payload>.*)</p>')
    matches = re.search(pattern, text).groupdict()

    return html.unescape(matches.get('payload', None))


class CctvApi(object):
    """
    >>> api = CctvApi()
    >>> api.get_data_for_location('Glasgow_Green_monument', '2020-06-07', '2020-06-07')
    ...
    """
    API_URL = 'https://api.ubdc.ac.uk/cctv'

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        self.username = username
        self.password = password

        self._session: requests.Session = requests.Session()
        self._session.headers = {
            "accept": "application/json",
            "content-type": "application/json; charset=UTF-8",
            "accept-encoding": "br, gzip, deflate"
        }
        if self.username and self.password:
            self._session.auth = (self.username, self.password)

    def __del__(self):
        if self._session:
            self._session.close()

    def get_data_for_location(self, location: str, from_date: str, to_date: str) -> dict[str, dict[str, str]]:
        """
        Return a dictionary with the result of the query

        :param location: The location to query
        :param from_date: DD/MM/YYYY. Start date
        :param to_date: DD/MM/YYYY. End date
        :return:
        """

        if location not in LOCATIONS:
            raise ValueError(f'Not valid location. {location}')
        r = self._session.get(self.API_URL + f"/counts/{location}/{from_date}/{to_date}")
        r.raise_for_status()

        payload = _extract_payload(r.text)
        payload = html.unescape(payload)
        if payload is None:
            raise ValueError('Payload was None')
        try:
            data = json.loads(payload)
        except json.decoder.JSONDecodeError:
            raise ValueError('The payload was not a json representation')
        except:
            raise Exception(f'Unknown error: {sys.exc_info()[0]}')
        return data
