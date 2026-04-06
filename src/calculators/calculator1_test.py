from typing import Dict, Any
from .calculator_1 import Calculator1
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self) -> Dict:
        return self.json


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator1 = Calculator1()

    result = calculator1.calculate(mock_request)

    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]

    assert result["data"]["result"] == 14.25
    assert result["data"]["calculator"] == "calculator_1"


def test_calculate_with_body_error():
    mock_request = MockRequest(body={})
    calculator1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator1.calculate(mock_request)

    assert "body mal formatado" in str(excinfo.value)
