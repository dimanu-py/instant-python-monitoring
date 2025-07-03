import time
from collections.abc import Generator

import pytest
import requests
from testcontainers.core.waiting_utils import wait_for_logs

from src.driven.for_sending_usage.loki_client import LokiClient
from test.driven.for_sending_usage.loki_test_container import LokiTestContainer


@pytest.fixture(scope="module")
def loki_base_url() -> Generator[str, None]:
    with LokiTestContainer() as loki:
        wait_for_logs(
            container=loki,
            predicate="server listening on addresses",
            timeout=10,
        )
        yield loki.get_base_url()


@pytest.mark.integration
class TestLokiClientIntegration:
    @pytest.fixture(autouse=True)
    def setup_method(self, loki_base_url: str) -> None:
        self._loki_url = loki_base_url
        self._client = LokiClient(self._loki_url)

    def test_loki_client_integration(self) -> None:
        info = {
            "command": "init",
            "version": "0.7.1",
            "platform": "linux",
            "template_data": {
                "name": "integration_test",
                "built_in_features": ["logger", "makefile"],
            },
        }

        self._client.send_information(info)
        time.sleep(2) 

        query = '{job="instant-python-monitoring"}'
        resp = requests.get(f"{self._loki_url}/loki/api/v1/query", params={"query": query})
        assert resp.status_code == 200
        data = resp.json()
        found = any("integration_test" in str(stream) for stream in str(data))
        assert found, f"Expected to find 'integration_test' in the Loki response: {data}"
