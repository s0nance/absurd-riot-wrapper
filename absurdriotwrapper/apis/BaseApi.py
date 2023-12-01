import requests.sessions
import logging


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
        return self._api_key

    def request(
        self, url: str, endpoint: str, method: str, region: str, query_params: dict
    ):
        query_params = {k: v for k, v in query_params.items() if v is not None}

        response = None

        if response is None:
            extra = {}

            response = self._session.get(
                url,
                params=query_params,
                headers={"X-Riot-Token": self._api_key},
                **extra
            )

        return response
