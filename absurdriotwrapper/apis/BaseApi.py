import requests.sessions
import logging


class BaseApi:
    """
    The base class to represent a Riot api.

    Determines the behavior of all subclasses.
    """

    def __init__(self, api_key):
        """
        Initializes a BaseApi instance with the provided Riot API key.

        Args:
            api_key (str): The Riot API key for authentication.
        """
        self._api_key = api_key
        self._session = requests.session()

    @property
    def api_key(self):
        """
        Property method to retrieve Riot API key.

        Returns:
            str: Riot API key
        """
        return self._api_key

    def request(
        self, url: str, endpoint: str, method: str, region: str, query_params: dict
    ):
        """
        Sends an HTTP request to the Riot API.

        Args:
            url (str): The URL of the Riot API.
            endpoint (str): The specific endpoint of the API.
            method (str): The HTTP method to be used.
            region (str): The region for which the request is made.
            query_params (dict): Parameters to be included in the API request.

        Returns:
            requests.Response: The response object from the API request.
        """
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
