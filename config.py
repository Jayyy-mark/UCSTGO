import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """Development configuration"""
    DEBUG = True
    # This uses SQLite for easy local testing. Change to PostgreSQL for production.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///ucstgo_dev.db'

class ProdConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:pass@localhost/ucstgo'

config_by_name = dict(dev=DevConfig, prod=ProdConfig)