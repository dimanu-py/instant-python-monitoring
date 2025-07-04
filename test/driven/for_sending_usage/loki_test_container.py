from testcontainers.core.container import DockerContainer


class LokiTestContainer(DockerContainer):
    _LOKI_IMAGE = "grafana/loki:3.4.4"
    _LOKI_PORT = 3100

    def __init__(self) -> None:
        super().__init__(self._LOKI_IMAGE)
        self.with_exposed_ports(self._LOKI_PORT)
        self.with_command(["-config.file=/etc/loki/local-config.yaml"])

    def get_base_url(self) -> str:
        host = self.get_container_host_ip()
        port = self.get_exposed_port(self._LOKI_PORT)
        return f"http://{host}:{port}"
