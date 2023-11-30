import requests.sessions


class BaseApi:
    """
    The base class to represent a Riot api.

    Determines the behavior of all subclasses.
    """

    def __init__(self, api_key):
        self._api_key = api_key
        self._session = requests.session()

    @property
    def api_key(self):
        return self.api_key

    def request(
            self,
            url: str,
            endpoint: str,
            method: str,
            region: str
    ):
        extra = {}

        response = self._session.get(
            url, headers={"X-Riot-Token": self._api_key},
            **extra
        )

        return response
