import os

class Config:
    UPLOAD_FOLDER = "uploads/"
    PDF_FOLDER = "salary_slips/"
    MONGO_URI = "mongodb://localhost:27017/"
    EMAIL_HOST = "sandbox.smtp.mailtrap.io"
    EMAIL_PORT = 587
    EMAIL_USER = "23d226ed95be75"
    EMAIL_PASS = "6c1d69b950a893"

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)
