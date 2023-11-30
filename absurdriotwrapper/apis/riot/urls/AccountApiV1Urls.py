from .RiotEndpoint import RiotEndpoint


class AccountV1Endpoint(RiotEndpoint):
    def __init__(self, url: str, **kwargs):
        super().__init__(f"/account/v1{url}", **kwargs)


class AccountApiV1Urls:
    by_puuid = AccountV1Endpoint("/accounts/by-puuid/{puuid}")
    by_riot_id = AccountV1Endpoint("/accounts/by-riot-id/{game_name}/{tag_line}")
    active_shard = AccountV1Endpoint("/active-shards/by-game/{game}/by-puuid/{puuid}")
    me = AccountV1Endpoint("/accounts/me")
