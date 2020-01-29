from ..core import LearnCubeBase


class Participants(LearnCubeBase):

    def __init__(self, public_key, private_key):

        super().__init__(public_key, private_key)

    def read_participant(self, uuid):
        response = self.get('participants/{}/'.format(uuid))
        if response.status_code != 200:
            raise Exception("Error during read", response.status_code, response.json())
        else:
            print(response.json())
            return response

    def list_participants(self, **kwargs):
        response = self.get('participants/', params=kwargs)
        if response.status_code != 200:
            raise Exception("Error during read", response.status_code, response.json())
        else:
            print(response.json())
            return response
