from json import JSONDecodeError
import requests
from requests import exceptions


class PypiException(Exception):
    def __init__(self, message, response_data=None):
        super().__init__(message)

        self.response_data = response_data

class Pypi(object):
    def __init__(self):
        self.api_url = 'https://pypi.org/pypi'

    def _call(self, path, method='GET'):
        url = '{}{}'.format(self.api_url, path)

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            else:
                raise Exception('Invalid method')
        except exceptions.RequestException as ex:
            raise PypiException("One or more packages doesn't exist")
                                            

        if response.status_code not in (200, 201):
            raise PypiException("One or more packages doesn't exist")
                                      

        return response.json()

    def check_package(self, package):
        if package.get('version',None):
            version = package.get('version')
            response = self._call(f'/{package.get("name")}/{version}/json')     
            return

        response = self._call(f'/{package.get("name")}/json') 
        releases = list(response.get('releases').keys())
        version = releases[-1]
        return version