"""
Utility functions for the Flask Contact Form Application
"""

import os


def get_message_count():
    """
    Helper function to count total messages in file

    Returns:
        int: The number of messages stored in messages.txt
    """
    try:
        if os.path.exists('messages.txt'):
            with open('messages.txt', 'r') as f:
                content = f.read()
                # Count separator lines as message indicators
                return content.count('=' * 50)
        return 0
    except Exception:
        return 0


def save_message(name, email, message, timestamp):
    """
    Save a message to the messages.txt file

    Args:
        name (str): The sender's name
        email (str): The sender's email address
        message (str): The message content
        timestamp (str): The timestamp when the message was submitted
    """
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Message: {message}\n")
