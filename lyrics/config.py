import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = r'efd9fd3b01364841ae7b431db9fca6a0'
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
