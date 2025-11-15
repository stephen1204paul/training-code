"""
Route handlers for the Flask Contact Form Application
"""

from flask import Blueprint, request, render_template
from datetime import datetime
import os

from .utils import get_message_count, save_message

# Create a Blueprint for routes
main = Blueprint('main', __name__)


@main.route('/')
def home():
    """Display the contact form"""
    return render_template('index.html')


@main.route('/submit', methods=['POST'])
def submit():
    """Process form submission and save to file"""
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validate data
        if not name or not email or not message:
            return render_template('error.html',
                                 error_title='Error',
                                 error_message='All fields are required!'), 400

        # Generate timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save to file
        save_message(name, email, message, timestamp)

        # Return success page
        return render_template('success.html',
                             name=name,
                             email=email,
                             timestamp=timestamp)

    except Exception as e:
        return render_template('error.html',
                             error_title='Server Error',
                             error_message=f'Something went wrong: {str(e)}'), 500


@main.route('/messages')
def view_messages():
    """View all submitted messages"""
    try:
        if not os.path.exists('messages.txt'):
            return render_template('no_messages.html')

        with open('messages.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        # Convert plain text to HTML with formatting
        html_content = content.replace('\n', '<br>').replace('='*50, '<hr>')

        return render_template('messages.html',
                             message_count=get_message_count(),
                             content=html_content)

    except Exception as e:
        return render_template('error.html',
                             error_title='Error',
                             error_message=f'Error reading messages: {str(e)}'), 500


@main.route('/health')
def health_check():
    """Simple health check endpoint"""
    return {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_messages': get_message_count(),
        'message_file_exists': os.path.exists('messages.txt')
    }
