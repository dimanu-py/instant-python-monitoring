import pytest
from expects import expect, equal, raise_error

from src.monitoring.shared.errors.incorrect_value_type import IncorrectValueType
from src.monitoring.shared.errors.required_value import RequiredValue
from src.monitoring.shared.value_objects.string_value_object import StringValueObject


@pytest.mark.unit
class TestStringValueObject:
    def test_should_create_string_value_object(self) -> None:
        value = "test string"

        string = StringValueObject(value)

        expect(string.value).to(equal(value))

    def test_should_raise_error_when_value_is_none(self) -> None:
        expect(lambda: StringValueObject(None)).to(raise_error(RequiredValue))  # type: ignore

    def test_should_raise_error_when_value_is_not_string(self) -> None:
        expect(lambda: StringValueObject(123)).to(raise_error(IncorrectValueType))  # type: ignore

    def test_should_compare_equal_with_same_value(self) -> None:
        common_value = "test string"
        first_string = StringValueObject(common_value)
        second_string = StringValueObject(common_value)

        expect(first_string).to(equal(second_string))

    def test_should_not_be_equal_with_different_values(self) -> None:
        first_string = StringValueObject("test1")
        second_string = StringValueObject("test2")

        expect(first_string).to_not(equal(second_string))
