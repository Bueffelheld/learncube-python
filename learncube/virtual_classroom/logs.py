from ..core import LearnCubeBase


class Logs(LearnCubeBase):

    def __init__(self, public_key, private_key):

        super().__init__(public_key, private_key)

    def read_logs(self, uuid):
        response = self.get('logs/{}/'.format(uuid))
        if response.status_code != 200:
            raise Exception("Error during read", response.status_code, response.json())
        else:
            print(response.json())
            return response

    def list_logs(self, **kwargs):
        response = self.get('logs/', params=kwargs)
        if response.status_code != 200:
            raise Exception("Error during read", response.status_code, response.json())
        else:
            print(response.json())
            return response
