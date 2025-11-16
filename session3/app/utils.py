"""
Utility functions for the Flask Contact Form Application
Supports both file-based storage and database (PostgreSQL/SQLite) via SQLAlchemy
"""

import os
from flask import current_app
from .models import Message


def get_message_count():
    """
    Helper function to count total messages

    Returns:
        int: The number of messages stored
    """
    try:
        # Use database if enabled
        if current_app.config.get('USE_DATABASE', False):
            return Message.count_all()

        # Fallback to file-based storage
        if os.path.exists('messages.txt'):
            with open('messages.txt', 'r') as f:
                content = f.read()
                # Count separator lines as message indicators
                return content.count('=' * 50)
        return 0
    except Exception as e:
        print(f"Error getting message count: {e}")
        return 0


def save_message(name, email, message, timestamp=None):
    """
    Save a message to storage (database or file)

    Args:
        name (str): The sender's name
        email (str): The sender's email address
        message (str): The message content
        timestamp (str, optional): The timestamp (used only for file storage)

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Use database if enabled
        if current_app.config.get('USE_DATABASE', False):
            Message.create(name=name, email=email, message=message)
            return True

        # Fallback to file-based storage
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
        return True

    except Exception as e:
        print(f"Error saving message: {e}")
        return False


def get_all_messages():
    """
    Retrieve all messages from storage

    Returns:
        list or str: List of Message objects (database) or formatted string (file)
    """
    try:
        # Use database if enabled
        if current_app.config.get('USE_DATABASE', False):
            return Message.get_all()

        # Fallback to file-based storage
        if os.path.exists('messages.txt'):
            with open('messages.txt', 'r', encoding='utf-8') as f:
                return f.read()
        return None

    except Exception as e:
        print(f"Error retrieving messages: {e}")
        return None


def format_messages_for_display(messages):
    """
    Format messages for HTML display

    Args:
        messages: Either a list of Message objects (database) or string (file)

    Returns:
        str: HTML-formatted message content
    """
    try:
        # If messages is a list of Message objects from database
        if isinstance(messages, list) and messages and hasattr(messages[0], 'to_dict'):
            html_parts = []
            for msg in messages:
                msg_dict = msg.to_dict()
                html_parts.append(f"""
                    <div class="message-item">
                        <strong>Name:</strong> {msg_dict.get('name', 'N/A')}<br>
                        <strong>Email:</strong> {msg_dict.get('email', 'N/A')}<br>
                        <strong>Message:</strong> {msg_dict.get('message', 'N/A')}<br>
                        <strong>Timestamp:</strong> {msg_dict.get('created_at', 'N/A')}
                    </div>
                    <hr>
                """)
            return ''.join(html_parts)

        # If messages is a string (from file), convert to HTML
        elif isinstance(messages, str):
            return messages.replace('\n', '<br>').replace('='*50, '<hr>')

        return "No messages available"

    except Exception as e:
        print(f"Error formatting messages: {e}")
        return "Error displaying messages"
