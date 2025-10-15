import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "1073676799")
    DB_NAME = os.getenv("DB_NAME", "makeup_lj")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )


class ProductionConfig(Config):
    DEBUG = False
    DB_HOST = "dpg-d3niihruibrs738efnhg-a"
    DB_PORT = 5432
    DB_USER = "root"
    DB_PASSWORD = "jS2AcESz6aNQBXbEUifj0GoDz9GnErTX"
    DB_NAME = "systemcontrol"

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
