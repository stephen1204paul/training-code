"""
Configuration settings for the Flask Contact Form Application
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class"""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False

    # Server settings
    HOST = '0.0.0.0'
    PORT = 8000

    # Application settings
    MESSAGE_FILE = 'messages.txt'

    # Database settings
    USE_DATABASE = os.environ.get('USE_DATABASE', 'false').lower() == 'true'

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Set to True to see SQL queries in console

    # Database URL - supports both Supabase and local PostgreSQL
    # Format: postgresql://user:password@host:port/database
    DATABASE_URL = os.environ.get('DATABASE_URL')

    # If DATABASE_URL is not set, construct from Supabase components
    if not DATABASE_URL and os.environ.get('SUPABASE_DB_URL'):
        DATABASE_URL = os.environ.get('SUPABASE_DB_URL')

    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///messages.db'  # Fallback to SQLite

    # Supabase settings (optional - for using Supabase client features like auth, storage, realtime)
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Show SQL queries in development


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    # In production, ensure SECRET_KEY and DATABASE_URL are set via environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not Config.DATABASE_URL:
        raise ValueError("DATABASE_URL must be set in production")


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory SQLite for testing
    WTF_CSRF_ENABLED = False


# Configuration dictionary for easy access
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
