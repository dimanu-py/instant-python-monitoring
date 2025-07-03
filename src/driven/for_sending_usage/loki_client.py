import json
import time

import requests

from src.monitoring.driven.for_sending_usage.for_sending_usage import ForSendingUsage


class LokiClient(ForSendingUsage):
    def __init__(self, url: str) -> None:
        self._push_endpoint = f"{url}/loki/api/v1/push"

    def send_information(self, info: dict) -> None:
        current_time_ns = int(time.time_ns())
        
        payload = {
            "streams": [
                {
                    "stream": {
                        "job": "command-usage",
                        "command": info["command"],
                        "version": info["version"],
                    },
                    "values": [
                        [str(current_time_ns), json.dumps(info)]
                    ]
                }
            ]
        }
        
        response = requests.post(
            self._push_endpoint,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code != 204:
            error_msg = f"Failed to send data to Loki: {response.status_code} - {response.text}"
            raise RuntimeError(error_msg)
