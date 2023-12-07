from .. import BaseApi, FormattedEndpoint
from .urls import ChampionApiV3Urls


class ChampionApiV3(FormattedEndpoint):
    def __init__(self, base_api: BaseApi):
        super().__init__(base_api, self.__class__.__name__)

    def champion_rotations(self, region: str):
        return self._request_endpoint(
            self.champion_rotations.__name__,
            region,
            ChampionApiV3Urls.champion_rotations,
        )
