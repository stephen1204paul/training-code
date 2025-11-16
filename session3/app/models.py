"""
Database models for the Flask Contact Form Application
Using SQLAlchemy ORM for database operations
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()


class Message(db.Model):
    """
    Message model for storing contact form submissions

    Attributes:
        id: Primary key, auto-incrementing integer
        name: Sender's name (required)
        email: Sender's email address (required)
        message: Message content (required)
        created_at: Timestamp when message was created
        updated_at: Timestamp when message was last updated
    """

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        """String representation of Message object"""
        return f'<Message {self.id}: {self.name} ({self.email})>'

    def to_dict(self):
        """
        Convert Message object to dictionary

        Returns:
            dict: Message data as dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, name, email, message):
        """
        Create a new message

        Args:
            name (str): Sender's name
            email (str): Sender's email
            message (str): Message content

        Returns:
            Message: The created message object
        """
        new_message = cls(
            name=name,
            email=email,
            message=message
        )
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @classmethod
    def get_all(cls, limit=None):
        """
        Get all messages, ordered by creation date (newest first)

        Args:
            limit (int, optional): Maximum number of messages to return

        Returns:
            list: List of Message objects
        """
        query = cls.query.order_by(cls.created_at.desc())
        if limit:
            query = query.limit(limit)
        return query.all()

    @classmethod
    def get_by_id(cls, message_id):
        """
        Get a message by ID

        Args:
            message_id (int): The message ID

        Returns:
            Message: The message object or None if not found
        """
        return cls.query.get(message_id)

    @classmethod
    def count_all(cls):
        """
        Get total count of messages

        Returns:
            int: Total number of messages
        """
        return cls.query.count()

    @classmethod
    def search(cls, search_term):
        """
        Search messages by name, email, or message content

        Args:
            search_term (str): The term to search for

        Returns:
            list: List of matching Message objects
        """
        search_pattern = f'%{search_term}%'
        return cls.query.filter(
            db.or_(
                cls.name.ilike(search_pattern),
                cls.email.ilike(search_pattern),
                cls.message.ilike(search_pattern)
            )
        ).order_by(cls.created_at.desc()).all()

    def update(self, **kwargs):
        """
        Update message fields

        Args:
            **kwargs: Field names and values to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        db.session.commit()

    def delete(self):
        """Delete this message"""
        db.session.delete(self)
        db.session.commit()
