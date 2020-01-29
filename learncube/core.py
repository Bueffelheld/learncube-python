import requests


class LearnCubeBase:
    _API_BASE_PATH = 'https://app.learncube_1.com/api/virtual-classroom/{}'
    last_valid_token = None

    def __init__(self, public_key, private_key):
        self._PUBLIC_KEY = public_key
        self._PRIVATE_KEY = private_key

    def _get_valid_token(self):
        # check if token is valid
        data = {"token": self.last_valid_token}
        response = requests.post(self._API_BASE_PATH.format('verify-api-token/'), json=data)
        if response.status_code != 200:
            # create token
            data = {"api_public_key": self._PUBLIC_KEY, "api_private_key": self._PRIVATE_KEY}
            response = requests.post(self._API_BASE_PATH.format('get-api-token/'), json=data)
            self.last_valid_token = response.json()['token']

        return self.last_valid_token

    def get(self, endpoint, params=None):
        if params is None:
            params = {}

        headers = {'Authorization': 'Bearer ' + self._get_valid_token()}
        response = requests.get(self._API_BASE_PATH.format(endpoint), headers=headers, params=params)
        return response

    def post(self, endpoint, json):
        headers = {'Authorization': 'Bearer ' + self._get_valid_token()}
        response = requests.post(self._API_BASE_PATH.format(endpoint), json=json, headers=headers)
        return response

    def put(self, endpoint, json):
        headers = {'Authorization': 'Bearer ' + self._get_valid_token()}
        response = requests.put(self._API_BASE_PATH.format(endpoint), json=json, headers=headers)
        return response

    def delete(self, endpoint):
        headers = {'Authorization': 'Bearer ' + self._get_valid_token()}
        response = requests.delete(self._API_BASE_PATH.format(endpoint), headers=headers)
        return response
