"""
Route handlers for the Flask Contact Form Application
"""

from flask import Blueprint, request, render_template, current_app
from datetime import datetime
import os

from .utils import get_message_count, save_message, get_all_messages, format_messages_for_display

# Create a Blueprint for routes
main = Blueprint('main', __name__)


@main.route('/')
def home():
    """Display the contact form"""
    return render_template('index.html')


@main.route('/submit', methods=['POST'])
def submit():
    """Process form submission and save to storage"""
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

        # Save to storage (Supabase or file)
        success = save_message(name, email, message, timestamp)

        if not success:
            return render_template('error.html',
                                 error_title='Server Error',
                                 error_message='Failed to save message. Please try again.'), 500

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
        # Get messages from storage
        messages = get_all_messages()

        # Check if no messages exist
        if not messages or (isinstance(messages, list) and len(messages) == 0):
            return render_template('no_messages.html')

        # Format messages for display
        html_content = format_messages_for_display(messages)

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
    use_database = current_app.config.get('USE_DATABASE', False)

    health_data = {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_messages': get_message_count(),
        'storage_type': 'database' if use_database else 'file',
    }

    # Add file existence check only if not using database
    if not use_database:
        health_data['message_file_exists'] = os.path.exists('messages.txt')
    else:
        # Add database info if using database
        db_uri = current_app.config.get('SQLALCHEMY_DATABASE_URI', '')
        if 'postgresql' in db_uri:
            health_data['database_type'] = 'postgresql'
        elif 'sqlite' in db_uri:
            health_data['database_type'] = 'sqlite'

    return health_data
