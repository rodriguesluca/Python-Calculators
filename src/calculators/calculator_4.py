from flask import request as FlaskRequest
from typing import List, Dict
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.get_json()
        input_data = self.__validate_body(body)

        average = self.__calculate_average(input_data)

        format_response = self.__format_response(average)
        return format_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "calculator": "calculator_4",
                "average": round(float(average), 2),
            }
        }
