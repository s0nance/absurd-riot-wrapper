import re


class Endpoint:
    def __init__(self, url: str, **kwargs):
        """
        Initializes an Endpoint instance with a URL pattern and extracts required and optional parameters.

        Args:
            url (str): The URL pattern with optional parameters enclosed in curly braces.
            **kwargs: Additional keyword arguments for initializing the Endpoint.

        Raises:
            ValueError: If the URL pattern contains empty parameter placeholders.

        Attributes:
            _url (str): The URL pattern for the endpoint.
            _url_params (list): List of required parameters extracted from the URL pattern.
            _query_params (list): List of optional parameters not included in the URL pattern.
        """
        self._url = url

        url_params = re.findall(r"{(\w*)}", self._url)

        if "" in url_params:
            raise ValueError("url params not good")

        self._url_params = url_params
        self._query_params = [key for key in kwargs if key not in url_params]

    def __call__(self, **kwargs):
        """
        Validates and formats the provided parameters to generate a complete URL and query parameters.

        Args:
            **kwargs: Keyword arguments representing parameters for the URL and query.

        Raises:
            ValueError: If a required parameter is missing.

        Returns:
            tuple: A tuple containing the formatted URL and query parameters.
        """
        for req_param in self._url_params:
            if req_param not in kwargs:
                raise ValueError(f'frérot le paramètre "{req_param} est requis kefa?')

        query_params = {
            key: value for key, value in kwargs.items() if key in self._query_params
        }
        return self._url.format(**kwargs), query_params
