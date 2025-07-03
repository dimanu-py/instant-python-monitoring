import json
import time
from collections.abc import Generator

import pytest
import requests
from expects import expect, be, equal
from testcontainers.core.waiting_utils import wait_for_logs

from src.driven.for_sending_usage.loki_client import LokiClient
from src.monitoring.usage.usage_information import UsageInformation
from test.driven.for_sending_usage.loki_test_container import LokiTestContainer
from test.monitoring.usage.usage_information_primitives_mother import (
    UsageInformationPrimitivesMother,
)


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
        info_primitives = UsageInformationPrimitivesMother.any()
        info = UsageInformation(**info_primitives)

        self._client.send_information(info)

        registered_information = self._wait_for_saved_data()
        expect(registered_information).to(equal(info_primitives))

    def _wait_for_saved_data(self) -> dict:
        time.sleep(2)  # Wait for Loki to ingest
        current_time = int(time.time())
        registered_information_response = requests.get(
            f"{self._loki_url}/loki/api/v1/query_range",
            params={
                "query": '{job="command-usage"}',
                "start": current_time - 60,
                "end": current_time,
                "limit": 100,
            },
        )

        expect(registered_information_response.status_code).to(be(200))
        registered_information_as_json = registered_information_response.json()
        return json.loads(
            registered_information_as_json["data"]["result"][0]["values"][0][1]
        )
