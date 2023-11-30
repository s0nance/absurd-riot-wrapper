from absurdriotwrapper.apis import BaseApi
from absurdriotwrapper.apis.lol import SummonerApiV4


class AbsurdLolWrapper:
    """
    A class that wraps the league of legends apis.
    """

    def __init__(self, api_key: str, **kwargs):
        """
        Instantiates a new AbsurdLolWrapper
        :param api_key: the api key to use for this instance
        :param kwargs: additional keyword arguments
        """

        if not api_key:
            raise ValueError("api key must be provided")

        self._base_api = BaseApi(api_key)
        self._summoner = SummonerApiV4(self._base_api)

    @property
    def summoner(self) -> SummonerApiV4:
        """
        Interacts with the SummonerV4 league api.
        :rtype: lol.SummonerApiV4
        """
        return self._summoner
