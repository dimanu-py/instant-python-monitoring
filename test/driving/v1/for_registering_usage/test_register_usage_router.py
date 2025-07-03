import pytest
from expects import expect, be
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse

from src.driving.application import app


@pytest.mark.acceptance
class TestRegisterUsageRouter:
    def setup_method(self) -> None:
        self._client = TestClient(app)
        self._response = JSONResponse(content={})

    def test_should_register_usage_of_instant_python_command(self) -> None:
        request_body = {
            "command": "init",
            "version": "0.7.0",
            "platform": "linux",
            "template_data": {
                "name": "clean_architecture",
                "built_in_features": ["value_objects", "logger"],
            },
        }

        self._response = self._when_a_post_request_is_made_to(
            "/app/v1/monitoring/usage", body=request_body
        )

        self._then_response_should_be_no_content()

    def _when_a_post_request_is_made_to(
        self, endpoint: str, body: dict
    ) -> JSONResponse:
        with self._client as client:
            return client.post(endpoint, json=body)  # type: ignore

    def _then_response_should_be_no_content(self) -> None:
        expect(self._response.status_code).to(be(204))
        expect(self._response.content).to(be(None))
