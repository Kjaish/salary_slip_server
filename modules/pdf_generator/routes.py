from flask import Blueprint, request, jsonify
import os
from modules.pdf_generator.utils import generate_pdf
from config import Config

pdf_blueprint = Blueprint("pdf", __name__)

@pdf_blueprint.route("/generate", methods=["POST"])
def generate_salary_slip():
    data = request.json
    filename = f"{data['employee_id']}.pdf"
    filepath = os.path.join(Config.PDF_FOLDER, filename)

    generate_pdf(data, filepath)
    return jsonify({"message": "PDF generated", "filename": filename}), 200
