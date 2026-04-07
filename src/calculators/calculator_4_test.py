from typing import Dict
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_4 import Calculator4
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self) -> Dict:
        return self.json


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(NumpyHandler())

    result = calculator_4.calculate(mock_request)

    mock_request_error = MockRequest({"algo_errado": 123})
    with raises(HttpUnprocessableEntityError) as exc_info:
        calculator_4.calculate(mock_request_error)

    assert str(exc_info.value) == "Unprocessable Entity: body mal formatado"

    assert result == {
        "data": {
            "calculator": "calculator_4",
            "average": 3.0,
        }
    }
