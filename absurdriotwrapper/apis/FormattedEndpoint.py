from . import BaseApi

from .Endpoint import Endpoint


class FormattedEndpoint:
    def __init__(self, base_api: BaseApi, endpoint: str):
        self._base_api = base_api
        self._endpoint = endpoint

    def _request_endpoint(self, method: str, region: str, endpoint: Endpoint, **kwargs):
        url, query = endpoint(platform=region, **kwargs)
        return self._base_api.request(url, self._endpoint, method, region)
