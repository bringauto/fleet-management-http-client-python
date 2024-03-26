from fleet_management_http_client_python import CarApi, PlatformHWApi, ApiApi, ApiClient, Configuration
from fleet_management_http_client_python import PlatformHW, Car


class ClientExample:
    """Example of Client of the Fleet Protocol HTTP API."""

    def __init__(self, host: str, api_key: str) -> None:
        """Create a new ClientExample.

        `host`: The host of the Fleet Protocol HTTP API.
        `api`: The API key to authenticate the client.
        """
        self._configuration = Configuration(host=host, api_key={"AdminAuth": api_key})
        self._api_client = ApiClient(self._configuration)
        self._car_api = CarApi(api_client=self._api_client)
        self._platform_hw_api = PlatformHWApi(api_client=self._api_client)
        self._api_api = ApiApi(api_client=self._api_client)

    def api_is_alive(self) -> bool:
        """Check if the API is alive."""
        try:
            response = self._api_api.check_api_is_alive_with_http_info()
            return response.status_code == 200
        except Exception:
            return False

    def get_cars(self) -> list[Car]:
        """Get all cars."""
        return self._car_api.get_cars()

    def get_platforms(self) -> list[PlatformHW]:
        """Get all platforms."""
        return self._platform_hw_api.get_hws()

