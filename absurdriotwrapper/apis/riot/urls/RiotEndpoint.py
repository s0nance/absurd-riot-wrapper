from ... import Endpoint, BaseUrl


class RiotEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/riot{url}"

    def __call__(self, **kwargs):
        url = f"{BaseUrl.base_riot_url}{self._url}"

        endpoint = Endpoint(url, **kwargs)
        return endpoint(**kwargs)
