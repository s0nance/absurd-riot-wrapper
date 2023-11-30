from .. import BaseApi, FormattedEndpoint
from .urls import SummonerApiV4Urls


class SummonerApiV4(FormattedEndpoint):
    def __init__(self, base_api: BaseApi):
        """
        Initializes a SummonerApiV4 instance.

        Args:
            base_api (BaseApi): The base API instance for making requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_name(self, region: str, summoner_name: str):
        """
        Retrieves summoner information by summoner name.

        Args:
            region (str): The region code (e.g., "na", "euw").
            summoner_name (str): The summoner name.

        Returns:
            Response: Summoner information.
        """
        return self._request_endpoint(
            self.by_name.__name__,
            region,
            SummonerApiV4Urls.by_name,
            summoner_name=summoner_name,
        )

    def by_account(self, region: str, encrypted_account_id: str):
        """
        Retrieves summoner information by encrypted account ID.

        Args:
            region (str): The region code (e.g., "na", "euw").
            encrypted_account_id (str): The encrypted account ID.

        Returns:
            dict: Summoner information.
        """
        return self._request_endpoint(
            self.by_account.__name__,
            region,
            SummonerApiV4Urls.by_account,
            encrypted_account_id=encrypted_account_id,
        )

    def by_puuid(self, region: str, encrypted_puuid: str):
        """
        Retrieves summoner information by encrypted PUUID.

        Args:
            region (str): The region code (e.g., "na", "euw").
            encrypted_puuid (str): The encrypted PUUID.

        Returns:
            dict: Summoner information.
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            SummonerApiV4Urls.by_puuid,
            encrypted_puuid=encrypted_puuid,
        )

    def me(self, region: str):
        """
        Retrieves summoner information for the current user.

        Args:
            region (str): The region code (e.g., "na", "euw").

        Returns:
            dict: Summoner information.
        """
        return self._request_endpoint(self.me.__name__, region, SummonerApiV4Urls.me)
