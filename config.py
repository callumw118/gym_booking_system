import os

class Config:
    SQLALCHEMY_DATABASEU_URI = os.environ.get('DATABASE_URL')