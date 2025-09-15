from urllib.parse import quote_plus

class Config:
    SECRET_KEY = 'super-secret-key'
    HOSTNAME = 'localhost'
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = quote_plus('MYSQL@246176')
    DATABASE = 'flaskxm'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
