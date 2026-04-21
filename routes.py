from flask import Blueprint, request, jsonify
from .pipeline import run_forecast

api_bp = Blueprint("api", __name__)

@api_bp.route("/forecast", methods=["POST"])
def forecast():
    data = request.get_json()
    model = data.get("model", "prophet")  # default to Prophet
    params = data.get("params", {})
    forecast_result = run_forecast(model, params)
    return jsonify(forecast_result)