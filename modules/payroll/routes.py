from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from config import Config

payroll_blueprint = Blueprint("payroll", __name__)
mongo_client = MongoClient(Config.MONGO_URI)
db = mongo_client["payroll_db"]
collection = db["payroll"]


@payroll_blueprint.route("/add", methods=["POST"])
def add_payroll():
    data = request.json
    response = collection.insert_one(data)
    return (
        jsonify(
            {"message": "Payroll record added", "emp_id": str(response.inserted_id)}
        ),
        201,
    )


@payroll_blueprint.route("/all", methods=["GET"])
def get_all_payroll():
    payrolls = list(collection.find({}, {"_id": 0}))
    return jsonify(payrolls), 200
