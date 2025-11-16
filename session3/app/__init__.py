"""
Flask Contact Form Application
Session 3: Virtual Machines & Cloud Compute
A simple web application demonstrating form handling, database migrations, and ORM usage
"""

from flask import Flask
from flask_migrate import Migrate
import os


def create_app(config_object='config.Config'):
    """
    Application factory function to create and configure the Flask app

    Args:
        config_object (str): The configuration object to use

    Returns:
        Flask: The configured Flask application instance
    """
    # Initialize Flask application
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    # Load configuration
    app.config.from_object(config_object)

    # Initialize SQLAlchemy
    from .models import db
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Print storage type
    if app.config.get('USE_DATABASE', False):
        db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
        if 'postgresql' in db_uri:
            # Extract host from DATABASE_URL for display
            if 'supabase' in db_uri:
                print(f"✅ Connected to Supabase PostgreSQL database")
            else:
                print(f"✅ Connected to PostgreSQL database")
        elif 'sqlite' in db_uri:
            print(f"✅ Using SQLite database: {db_uri.replace('sqlite:///', '')}")
        else:
            print(f"✅ Using database: {db_uri.split('@')[-1] if '@' in db_uri else 'configured'}")
    else:
        print("📁 Using file-based storage (messages.txt)")

    # Create tables if they don't exist (for development)
    # In production, use migrations instead
    with app.app_context():
        if app.config.get('USE_DATABASE', False):
            try:
                db.create_all()
                print("✅ Database tables verified/created")
            except Exception as e:
                print(f"⚠️  Database initialization warning: {e}")

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
