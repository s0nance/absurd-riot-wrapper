from ... import Endpoint, BaseUrl


class LolEndpoint:
    """
    A class to represent an Endpoint used for the league of legends api.
    """

    def __init__(self, url: str, **kwargs):
        """

        :param url: str
            the url of the endpoint.
        :param kwargs: additional keywords arguments.
        """
        self._url = f"/riot{url}"

    def __call__(self, **kwargs):
        """
        Constructs a complete URL by appending the specific endpoint URL to the base Riot URL.

        Args:
            **kwargs: Additional keyword arguments to be passed to the Endpoint constructor.

        Returns:
            Endpoint: An instance of the Endpoint class representing the constructed URL.

        Example:
            >>> YourCustomApiEndpointClass(LolEndpoint)
            >>> # This will allow your custom api endpoint class to use the desired enpoint, in this case the league of legends one.
        """

        url = f"{BaseUrl.base_riot_url}{self._url}"

        endpoint = Endpoint(url, **kwargs)
        return endpoint(**kwargs)
