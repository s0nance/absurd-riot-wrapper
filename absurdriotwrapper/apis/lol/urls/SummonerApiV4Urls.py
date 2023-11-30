from .LolEndpoint import LolEndpoint


class SummonerV4Endpoint(LolEndpoint):
    def __int__(self, url: str, **kwargs):
        """
        Initializes a SummonerV4Endpoint instance.

        Args:
            url (str): The specific endpoint URL for the Summoner API V4.
            **kwargs: Additional keyword arguments for initializing the endpoint.

        Note:
            The URL is formatted to include the base path for the Summoner API V4 ("/summoner/v4").

        Example:
            >>> summoner_endpoint = SummonerV4Endpoint("/some-endpoint")
        """
        super().__init__(f"/summoner/v4{url}", **kwargs)


class SummonerApiV4Urls:
    """
    Collection of Summoner API V4 endpoints.

    Used to create wrapper functions and make requests.
    """

    by_name = SummonerV4Endpoint("/summoners/by-name/{summoner_name}")
    by_account = SummonerV4Endpoint("/summoners/by-account/{encrypted_account_id}")
    by_puuid = SummonerV4Endpoint("/summoners/by-puuid/{encrypted_puuid}")
    me = SummonerV4Endpoint("/summoners/me")
