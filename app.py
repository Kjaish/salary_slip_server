from flask import Flask
from modules.upload.routes import upload_blueprint
from modules.payroll.routes import payroll_blueprint
from modules.pdf_generator.routes import pdf_blueprint
from modules.email_service.routes import email_blueprint
from config import Config
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(Config)

# Database connection
mongo_client = MongoClient(app.config["MONGO_URI"])
db = mongo_client["payroll_db"]

# Register Blueprints
app.register_blueprint(upload_blueprint, url_prefix="/api/upload")
app.register_blueprint(payroll_blueprint, url_prefix="/api/payroll")
app.register_blueprint(pdf_blueprint, url_prefix="/api/pdf")
app.register_blueprint(email_blueprint, url_prefix="/api/email")

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
