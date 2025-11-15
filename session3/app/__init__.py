"""
Flask Contact Form Application
Session 3: Virtual Machines & Cloud Compute
A simple web application demonstrating form handling and file I/O
"""

from flask import Flask
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

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
