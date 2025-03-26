from flask import Blueprint, request, jsonify
from modules.email_service.utils import send_email

email_blueprint = Blueprint("email", __name__)

@email_blueprint.route("/send", methods=["POST"])
def send_salary_slip():
    data = request.json
    employee_email = data["email"]
    pdf_filename = data["filename"]

    result = send_email(employee_email, pdf_filename)
    if result:
        return jsonify({"message": "Email sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send email"}), 500
