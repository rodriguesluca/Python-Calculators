from typing import Dict
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self) -> Dict:
        return self.json


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3]})
    calculator_3 = Calculator3(NumpyHandler())

    result = calculator_3.calculate(mock_request)

    mock_request_error = MockRequest({"algo_errado": 123})
    with raises(ValueError):
        calculator_3.calculate(mock_request_error)

    assert result == {
        "data": {
            "calculator": "calculator_3",
            "variance": 0.67,
            "multiplication": 6,
        }
    }
