import json
import time
from collections.abc import Generator

import pytest
import requests
from expects import expect, be, equal
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
        time.sleep(2)  # Wait for Loki to ingest

        query = '{job="command-usage"}'
        current_time = int(time.time())
        query_params = {
            "query": query,
            "start": current_time - 60,  # 60 seconds ago
            "end": current_time,        # now
            "limit": 100
        }
        registered_information_response = requests.get(f"{self._loki_url}/loki/api/v1/query_range", params=query_params)
        expect(registered_information_response.status_code).to(be(200))
        data = registered_information_response.json()
        registered_information_values = json.loads(data["data"]["result"][0]["values"][0][1])
        expect(registered_information_values).to(equal(info))

