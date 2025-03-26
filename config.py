import os

class Config:
    UPLOAD_FOLDER = "uploads/"
    PDF_FOLDER = "salary_slips/"

    MONGO_URI = "mongodb+srv://jackinitekadiwal:afdaUUmbP32Pbnt0@mycluster.rtt34.mongodb.net/payroll_db?retryWrites=true&w=majority"
    # MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    EMAIL_HOST = os.getenv("SMTP_HOST", "sandbox.smtp.mailtrap.io")
    EMAIL_PORT = os.getenv("SMTP_PORT", 587)
    # EMAIL_PORT = os.getenv("SMTP_PORT")
    EMAIL_USER = "c6343bc5e70ad3"
    # EMAIL_USER = os.getenv("USERNAME")
    EMAIL_PASS = "5b466023a788a6"
    # EMAIL_PASS = os.getenv("PASSWORD")

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)
