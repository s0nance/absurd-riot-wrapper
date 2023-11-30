from .. import BaseApi, FormattedEndpoint
from .urls import AccountApiV1Urls


class AccountApiV1(FormattedEndpoint):
    def __init__(self, base_api: BaseApi):
        super().__init__(base_api, self.__class__.__name__)

    def by_puuid(self, region: str, puuid: str):
        return self._request_endpoint(
            self.by_puuid.__name__, region, AccountApiV1Urls.by_puuid, puuid=puuid
        )

    def by_riot_id(self, region: str, game_name: str, tag_line: str):
        return self._request_endpoint(
            self.by_riot_id.__name__,
            region,
            AccountApiV1Urls.by_riot_id,
            game_name=game_name,
            tag_line=tag_line,
        )
