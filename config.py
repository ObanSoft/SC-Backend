import os

class Config:
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "1073676799")
    DB_NAME = os.environ.get("DB_NAME", "makeup_lj")
    SECRET_KEY = os.environ.get("SECRET_KEY", "JS65D7xdcYcX")