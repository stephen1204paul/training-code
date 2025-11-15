"""
Flask Contact Form Application
Session 3: Virtual Machines & Cloud Compute
A simple web application demonstrating form handling and file I/O
"""

from flask import Flask, request, render_template_string
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# HTML template for the contact form
FORM_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Session 3</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }
        
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }
        
        input, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 14px;
            transition: border-color 0.3s;
            font-family: inherit;
        }
        
        input:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .footer {
            margin-top: 20px;
            text-align: center;
            color: #999;
            font-size: 12px;
        }
        
        .footer a {
            color: #667eea;
            text-decoration: none;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📧 Contact Us</h1>
        <p class="subtitle">Send us a message and we'll get back to you soon!</p>
        
        <form action="/submit" method="POST">
            <div class="form-group">
                <label for="name">Your Name *</label>
                <input type="text" id="name" name="name" required 
                       placeholder="Enter your full name">
            </div>
            
            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email" required 
                       placeholder="your.email@example.com">
            </div>
            
            <div class="form-group">
                <label for="message">Your Message *</label>
                <textarea id="message" name="message" required 
                          placeholder="Tell us what's on your mind..."></textarea>
            </div>
            
            <button type="submit">Send Message ✉️</button>
        </form>
        
        <div class="footer">
            <p>Session 3 - Cloud Computing Course</p>
            <p><a href="/messages">View All Messages</a></p>
        </div>
    </div>
</body>
</html>
"""


def get_message_count():
    """Helper function to count total messages in file"""
    try:
        if os.path.exists('messages.txt'):
            with open('messages.txt', 'r') as f:
                content = f.read()
                # Count separator lines as message indicators
                return content.count('=' * 50)
        return 0
    except Exception:
        return 0


@app.route('/')
def home():
    """Display the contact form"""
    return render_template_string(FORM_HTML)


@app.route('/submit', methods=['POST'])
def submit():
    """Process form submission and save to file"""
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate data
        if not name or not email or not message:
            return """
            <html>
            <head><style>body{font-family:Arial; text-align:center; padding:50px;
                               background:#f44336; color:white;}</style></head>
            <body>
                <h1>❌ Error</h1>
                <p>All fields are required!</p>
                <a href="/" style="color:white;">Go Back</a>
            </body>
            </html>
            """, 400
        
        # Generate timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save to file
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
        
        # Return success page
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }}
                .success-container {{
                    background: white;
                    padding: 50px;
                    border-radius: 10px;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    text-align: center;
                    max-width: 500px;
                }}
                h1 {{
                    color: #11998e;
                    font-size: 48px;
                    margin-bottom: 20px;
                }}
                p {{
                    color: #666;
                    font-size: 18px;
                    margin: 15px 0;
                }}
                .info {{
                    background: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 30px;
                    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: 600;
                    transition: transform 0.2s;
                }}
                a:hover {{
                    transform: translateY(-2px);
                }}
            </style>
        </head>
        <body>
            <div class="success-container">
                <h1>✅</h1>
                <h2>Message Received!</h2>
                <p>Thanks <strong>{name}</strong>!</p>
                <div class="info">
                    <p>We'll contact you at:<br><strong>{email}</strong></p>
                </div>
                <p style="font-size: 14px; color: #999;">
                    Submitted at {timestamp}
                </p>
                <a href="/">Send Another Message</a>
            </div>
        </body>
        </html>
        """
        
    except Exception as e:
        return f"""
        <html>
        <head><style>body{{font-family:Arial; text-align:center; padding:50px;
                           background:#f44336; color:white;}}</style></head>
        <body>
            <h1>❌ Server Error</h1>
            <p>Something went wrong: {str(e)}</p>
            <a href="/" style="color:white;">Go Back</a>
        </body>
        </html>
        """, 500


@app.route('/messages')
def view_messages():
    """View all submitted messages"""
    try:
        if not os.path.exists('messages.txt'):
            return """
            <html>
            <head><style>body{font-family:Arial; text-align:center; padding:50px;}</style></head>
            <body>
                <h1>📭 No Messages Yet</h1>
                <p>No messages have been submitted yet.</p>
                <a href='/'>Send the first message</a>
            </body>
            </html>
            """
        
        with open('messages.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert plain text to HTML with formatting
        html_content = content.replace('\n', '<br>').replace('='*50, '<hr>')
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f5f5f5;
                    padding: 20px;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #333;
                    border-bottom: 3px solid #667eea;
                    padding-bottom: 10px;
                }}
                .content {{
                    font-family: 'Courier New', monospace;
                    font-size: 14px;
                    line-height: 1.6;
                    white-space: pre-wrap;
                    background: #f9f9f9;
                    padding: 20px;
                    border-radius: 5px;
                    border-left: 4px solid #667eea;
                }}
                hr {{
                    border: none;
                    border-top: 2px solid #667eea;
                    margin: 20px 0;
                }}
                .footer {{
                    margin-top: 20px;
                    text-align: center;
                }}
                a {{
                    display: inline-block;
                    padding: 10px 20px;
                    background: #667eea;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 5px;
                }}
                a:hover {{
                    background: #5568d3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📨 All Submitted Messages</h1>
                <p><strong>Total Messages:</strong> {get_message_count()}</p>
                <div class="content">{html_content}</div>
                <div class="footer">
                    <a href="/">Submit New Message</a>
                    <a href="/health">Health Check</a>
                </div>
            </div>
        </body>
        </html>
        """
        
    except Exception as e:
        return f"<h1>Error reading messages:</h1><p>{str(e)}</p><a href='/'>Go Back</a>", 500


@app.route('/health')
def health_check():
    """Simple health check endpoint"""
    return {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_messages': get_message_count(),
        'message_file_exists': os.path.exists('messages.txt')
    }


if __name__ == '__main__':
    # Print startup information
    print("\n" + "=" * 50)
    print("🚀 Flask Contact Form Application")
    print("=" * 50)
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"📧 Total messages: {get_message_count()}")
    print("\n🌐 Access your application at:")
    print("   http://localhost:8000/")
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
    # debug=True enables auto-reload and detailed error pages
    app.run(host='0.0.0.0', port=8000, debug=True)