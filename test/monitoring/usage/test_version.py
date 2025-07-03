import pytest
from expects import expect, raise_error

from src.monitoring.usage.invalid_version_format import InvalidVersionFormat
from src.monitoring.usage.version import Version


@pytest.mark.unit
class TestVersion:
    @pytest.mark.parametrize(
        "invalid_version",
        [
            pytest.param("a.b.c", id="non-numeric"),
            pytest.param("1.2", id="missing_patch"),
            pytest.param("1.2.", id="trailing_dot"),
            pytest.param("1-2-3", id="dashes_instead_of_dots"),
        ],
    )
    def test_should_raise_error_when_version_does_not_match_format(
        self, invalid_version: str
    ) -> None:
        expect(lambda: Version(invalid_version)).to(raise_error(InvalidVersionFormat))
