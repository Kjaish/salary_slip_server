from flask import Blueprint, request, jsonify, current_app
import pandas as pd
import os
from modules.upload.utils import parse_excel

upload_blueprint = Blueprint("upload", __name__)

@upload_blueprint.route("/file", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        parsed_data = parse_excel(filepath)
        return jsonify({"message": "File processed", "data": parsed_data}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid file."}), 500
