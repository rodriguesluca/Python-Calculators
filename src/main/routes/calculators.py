from flask import Blueprint, request, jsonify
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator4_factory import calculator4_factory

from src.errors.error_controler import handle_error

calc_route_bp = Blueprint("calc_route_bp", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        calc = calculator1_factory()
        result = calc.calculate(request)
        return jsonify({"success": True, "result": result}), 200
    except Exception as exc:
        response = handle_error(exc)
        return jsonify(response["body"]), response["status_code"]


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        calc = calculator2_factory()
        result = calc.calculate(request)
        return jsonify({"success": True, "result": result}), 200
    except Exception as exc:
        response = handle_error(exc)
        return jsonify(response["body"]), response["status_code"]


@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        calc = calculator3_factory()
        result = calc.calculate(request)
        return jsonify({"success": True, "result": result}), 200
    except Exception as exc:
        response = handle_error(exc)
        return jsonify(response["body"]), response["status_code"]


@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        calc = calculator4_factory()
        result = calc.calculate(request)
        return jsonify({"success": True, "result": result}), 200
    except Exception as exc:
        response = handle_error(exc)
        return jsonify(response["body"]), response["status_code"]
