import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = r'efd9fd3b01364841ae7b431db9fca6a0'
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
SQLALCHEMY_ECHO=True
REDIS_HOST=os.environ['REDIS_HOST']
FLASK_ADMIN_SWATCH = 'cerulean'
INCOGNITO_PIC_ADDRESS='https://artsiom-kushniarou-pics.s3.us-east-2.amazonaws.com/download.png'
S3_BUCKET=os.environ.get("S3_BUCKET")
S3_KEY=os.environ.get("S3_KEY")
S3_SECRET=os.environ.get("S3_SECRET")
S3_LOCATION='http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
