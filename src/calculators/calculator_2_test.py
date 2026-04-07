from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self) -> Dict:
        return self.json


class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return 9

    def average(self, numbers: List[float]) -> float:
        return 3


class TestCalculator2:
    def test_calculate(self):
        driver = MockDriverHandler()
        calc2 = Calculator2(driver)
        request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
        result = calc2.calculate(request)
        print()
        print(result)

        assert isinstance(result, dict)
        assert result == {"data": {"calculator": "calculator_2", "result": 0.33}}
