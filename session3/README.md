# Flask Contact Form Application

## Session 3: Virtual Machines & Cloud Compute

A professionally structured Flask web application demonstrating best practices in web development, form handling, and file I/O operations. This project showcases a production-ready architecture with proper separation of concerns.

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Using the Application](#using-the-application)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Architecture & Design Patterns](#architecture--design-patterns)
- [Troubleshooting](#troubleshooting)
- [Deployment](#deployment)

## Overview

This application provides a simple yet robust contact form that:
- Accepts user submissions (name, email, message)
- Validates input data
- Stores messages in a text file
- Displays all submitted messages
- Provides a health check endpoint for monitoring

**Key Technologies:**
- Python 3.x
- Flask 3.0.0 (Web Framework)
- Jinja2 (Template Engine)
- HTML5 & CSS3

## Learning Objectives

By the end of this session, you will understand:

1. **Web Application Architecture**
   - MVC (Model-View-Controller) pattern
   - Application factory pattern
   - Blueprint-based routing

2. **Flask Best Practices**
   - Proper project structure
   - Separation of concerns
   - Configuration management
   - Template inheritance

3. **Cloud Deployment Readiness**
   - Environment-specific configurations
   - Health check endpoints
   - Logging and monitoring setup
   - Static file serving

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
  ```bash
  python --version  # Should show 3.8+
  ```

- **pip** (Python package installer)
  ```bash
  pip --version
  ```

- **Optional but Recommended:**
  - Virtual environment tool (`venv` or `virtualenv`)
  - Git for version control

## Project Structure

```
session3/
├── app.py                      # Application entry point
├── config.py                   # Configuration classes for different environments
├── requirements.txt            # Python dependencies
├── messages.txt               # Generated file (stores form submissions)
│
├── app/                       # Main application package
│   ├── __init__.py           # App factory function
│   ├── routes.py             # Route handlers (controllers)
│   └── utils.py              # Utility functions (message handling)
│
├── templates/                 # Jinja2 HTML templates (views)
│   ├── base.html             # Base template with common structure
│   ├── index.html            # Contact form page
│   ├── success.html          # Form submission success page
│   ├── messages.html         # Display all messages
│   ├── error.html            # Error page
│   └── no_messages.html      # Empty state page
│
└── static/                    # Static assets
    └── css/
        └── style.css         # Application styles
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main entry point that initializes and runs the Flask application |
| `config.py` | Contains configuration classes for dev/prod/test environments |
| `app/__init__.py` | Application factory that creates and configures the Flask app |
| `app/routes.py` | Defines all URL routes and their handler functions |
| `app/utils.py` | Helper functions for message storage and retrieval |
| `templates/*.html` | HTML templates using Jinja2 syntax |
| `static/css/style.css` | Cascading styles for the application |

## Installation

### Step 1: Navigate to Project Directory

```bash
cd training-code/session3
```

### Step 2: Create Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0 - Web framework
- Werkzeug 3.0.1 - WSGI utilities

### Step 4: Verify Installation

```bash
pip list
```

You should see Flask and Werkzeug in the list.

## Running the Application

### Development Mode (Default)

```bash
python app.py
```

**Output:**
```
==================================================
🚀 Flask Contact Form Application
==================================================
📁 Working directory: /path/to/session3
🔧 Environment: development
📧 Total messages: 0

🌐 Access your application at:
   http://localhost:8000/

📚 Available routes:
   GET  /          - Contact form
   POST /submit    - Submit form data
   GET  /messages  - View all messages
   GET  /health    - Health check

⚠️  Press Ctrl+C to stop the server
==================================================
```

### Production Mode

```bash
FLASK_ENV=production python app.py
```

**Or set environment variable permanently:**

**macOS/Linux:**
```bash
export FLASK_ENV=production
python app.py
```

**Windows:**
```bash
set FLASK_ENV=production
python app.py
```

### Custom Host/Port

Edit `config.py` to change the default host and port:
```python
HOST = '0.0.0.0'  # Accept connections from any IP
PORT = 8000       # Change to your preferred port
```

## Using the Application

### 1. Access the Contact Form

Open your web browser and navigate to:
```
http://localhost:8000/
```

### 2. Fill Out the Form

- **Name**: Enter your full name
- **Email**: Enter a valid email address
- **Message**: Type your message

### 3. Submit the Form

Click "Send Message" - you'll be redirected to a success page showing your submission details.

### 4. View All Messages

- Click "View All Messages" from the footer
- Or navigate to `http://localhost:8000/messages`

### 5. Check Application Health

Navigate to:
```
http://localhost:8000/health
```

**Sample Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-15T10:30:00.123456",
  "total_messages": 5,
  "message_file_exists": true
}
```

## API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | Display contact form | HTML page |
| POST | `/submit` | Submit form data | Success/Error HTML |
| GET | `/messages` | View all messages | HTML page |
| GET | `/health` | Health check | JSON object |

### Example: Submit Form Data

**Request:**
```bash
curl -X POST http://localhost:8000/submit \
  -d "name=John Doe" \
  -d "email=john@example.com" \
  -d "message=Hello World"
```

### Example: Health Check

**Request:**
```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-15T10:30:00.123456",
  "total_messages": 1,
  "message_file_exists": true
}
```

## Configuration

The application supports three environments:

### Development (Default)
- Debug mode: **ON**
- Auto-reload: **Enabled**
- Detailed error pages: **Yes**
- Secret key: Default dev key

### Production
- Debug mode: **OFF**
- Auto-reload: **Disabled**
- Secret key: **Must be set via environment variable**

**Set production secret key:**
```bash
export SECRET_KEY='your-super-secret-key-here'
export FLASK_ENV=production
python app.py
```

### Testing
- Testing mode: **ON**
- Debug mode: **ON**
- Used for automated tests

**Configuration Files:**
- `config.py` - Contains all configuration classes

## Architecture & Design Patterns

### 1. Application Factory Pattern
Located in `app/__init__.py`, the `create_app()` function creates and configures the Flask application. This allows for:
- Multiple app instances
- Easier testing
- Different configurations per environment

### 2. Blueprints
Routes are organized using Flask blueprints (`app/routes.py`), which:
- Modularize the application
- Make code reusable
- Simplify large applications

### 3. Template Inheritance
All templates extend `base.html`, which:
- Ensures consistent layout
- Reduces code duplication
- Makes maintenance easier

### 4. Separation of Concerns

**MVC Pattern:**
- **Models**: `utils.py` (data handling)
- **Views**: `templates/*.html` (presentation)
- **Controllers**: `routes.py` (business logic)

### 5. Configuration Management
Environment-specific settings in `config.py`:
- Development
- Production
- Testing

## Troubleshooting

### Issue: Port 8000 Already in Use

**Solution:**
```bash
# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9

# Or change the port in config.py
PORT = 8080
```

### Issue: Module Not Found Error

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Template Not Found

**Error:**
```
jinja2.exceptions.TemplateNotFound: index.html
```

**Solution:**
- Ensure you're running `python app.py` from the `session3/` directory
- Verify `templates/` folder exists with all HTML files

### Issue: Permission Denied on messages.txt

**Solution:**
```bash
chmod 666 messages.txt  # Give read/write permissions
```

### Issue: Browser Shows "Connection Refused"

**Solution:**
- Ensure the Flask server is running
- Check firewall settings
- Verify the correct port (8000)

## Deployment

### Deploying to Cloud Platforms

This application is ready for deployment to:
- **AWS EC2**
- **Google Cloud Compute Engine**
- **Azure Virtual Machines**
- **Heroku**
- **DigitalOcean**

### Pre-Deployment Checklist

- [ ] Set `FLASK_ENV=production`
- [ ] Set secure `SECRET_KEY` via environment variable
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Set up a reverse proxy (Nginx, Apache)
- [ ] Configure firewall rules
- [ ] Set up SSL/TLS certificates
- [ ] Configure logging
- [ ] Set up monitoring

### Example: Gunicorn Deployment

**Install Gunicorn:**
```bash
pip install gunicorn
```

**Run with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Example: Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/session3/static;
    }
}
```

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Deploying Flask Apps](https://flask.palletsprojects.com/en/3.0.x/deploying/)

## Session Information

- **Course**: Cloud Computing
- **Session**: 3 - Virtual Machines & Cloud Compute
- **Focus**: Web Application Structure & Deployment Best Practices
- **Duration**: 2-3 hours

---

**Need Help?** Review the troubleshooting section or check Flask documentation.
