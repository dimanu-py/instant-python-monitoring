import pytest
from expects import expect, equal, raise_error

from src.monitoring.shared.errors.incorrect_value_type import IncorrectValueType
from src.monitoring.shared.errors.required_value import RequiredValue
from src.monitoring.usage.missing_template_keys import MissingTemplateKeys
from src.monitoring.usage.template_data import TemplateData


@pytest.mark.unit
class TestTemplateData:
    def test_should_create_template_data_with_valid_dict(self) -> None:
        template_dict = {
            "name": "test-template",
            "built_in_features": ["feature1", "feature2"],
        }

        template_data = TemplateData(template_dict)

        expect(template_data.value).to(equal(template_dict))

    def test_should_raise_error_when_value_is_none(self) -> None:
        expect(lambda: TemplateData(None)).to(raise_error(RequiredValue))  # type: ignore

    def test_should_raise_error_when_value_is_not_dict(self) -> None:
        expect(lambda: TemplateData([])).to(raise_error(IncorrectValueType))  # type: ignore

    def test_should_raise_error_when_missing_required_keys(self) -> None:
        template_missing_key = {"built_in_features": ["feature1"]}

        expect(lambda: TemplateData(template_missing_key)).to(
            raise_error(MissingTemplateKeys)
        )

    def test_should_compare_equal_with_same_value(self) -> None:
        value = {"name": "test-template", "built_in_features": ["feature1", "feature2"]}

        first_template = TemplateData(value)
        second_template = TemplateData(value.copy())

        expect(first_template).to(equal(second_template))

    def test_should_not_be_equal_with_different_values(self) -> None:
        first_template = TemplateData(
            {"name": "template1", "built_in_features": ["feature1"]}
        )

        second_template = TemplateData(
            {"name": "template2", "built_in_features": ["feature2"]}
        )

        expect(first_template).to_not(equal(second_template))
