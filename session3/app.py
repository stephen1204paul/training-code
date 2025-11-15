"""
Flask Contact Form Application
Session 3: Virtual Machines & Cloud Compute
Main entry point for the application
"""

import os
from app import create_app
from app.utils import get_message_count
from config import config

# Get environment or use default
env = os.environ.get('FLASK_ENV', 'development')
app = create_app(config[env])

if __name__ == '__main__':
    # Print startup information
    print("\n" + "=" * 50)
    print("🚀 Flask Contact Form Application")
    print("=" * 50)
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🔧 Environment: {env}")
    print(f"📧 Total messages: {get_message_count()}")
    print("\n🌐 Access your application at:")
    print(f"   http://localhost:{app.config['PORT']}/")
    print("\n📚 Available routes:")
    print("   GET  /          - Contact form")
    print("   POST /submit    - Submit form data")
    print("   GET  /messages  - View all messages")
    print("   GET  /health    - Health check")
    print("\n⚠️  Press Ctrl+C to stop the server")
    print("=" * 50 + "\n")

    # Run the application
    # host='0.0.0.0' makes it accessible from any IP
    # port=8000 (changed from 5000 due to macOS AirPlay conflict)
    # debug mode from config enables auto-reload and detailed error pages
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])