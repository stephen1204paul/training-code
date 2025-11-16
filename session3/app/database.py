"""
Supabase database operations for the Flask Contact Form Application
"""

from supabase import create_client, Client
from typing import Optional, Dict, List
from datetime import datetime


class SupabaseDB:
    """Wrapper class for Supabase database operations"""

    def __init__(self, url: str, key: str):
        """
        Initialize Supabase client

        Args:
            url (str): Supabase project URL
            key (str): Supabase API key (anon or service role)
        """
        self.client: Client = create_client(url, key)
        self.table_name = 'messages'

    def save_message(self, name: str, email: str, message: str) -> Optional[Dict]:
        """
        Save a message to the Supabase database

        Args:
            name (str): The sender's name
            email (str): The sender's email address
            message (str): The message content

        Returns:
            Optional[Dict]: The inserted record or None if failed
        """
        try:
            data = {
                'name': name,
                'email': email,
                'message': message,
                'created_at': datetime.now().isoformat()
            }

            response = self.client.table(self.table_name).insert(data).execute()
            return response.data[0] if response.data else None

        except Exception as e:
            print(f"Error saving message to Supabase: {e}")
            return None

    def get_all_messages(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Retrieve all messages from the database

        Args:
            limit (Optional[int]): Maximum number of messages to retrieve

        Returns:
            List[Dict]: List of message records
        """
        try:
            query = self.client.table(self.table_name).select('*').order('created_at', desc=True)

            if limit:
                query = query.limit(limit)

            response = query.execute()
            return response.data if response.data else []

        except Exception as e:
            print(f"Error retrieving messages from Supabase: {e}")
            return []

    def get_message_count(self) -> int:
        """
        Get the total count of messages in the database

        Returns:
            int: The number of messages
        """
        try:
            response = self.client.table(self.table_name).select('id', count='exact').execute()
            return response.count if hasattr(response, 'count') else 0

        except Exception as e:
            print(f"Error counting messages in Supabase: {e}")
            return 0

    def get_message_by_id(self, message_id: int) -> Optional[Dict]:
        """
        Retrieve a specific message by ID

        Args:
            message_id (int): The message ID

        Returns:
            Optional[Dict]: The message record or None if not found
        """
        try:
            response = self.client.table(self.table_name).select('*').eq('id', message_id).execute()
            return response.data[0] if response.data else None

        except Exception as e:
            print(f"Error retrieving message by ID from Supabase: {e}")
            return None

    def delete_message(self, message_id: int) -> bool:
        """
        Delete a message by ID

        Args:
            message_id (int): The message ID to delete

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            response = self.client.table(self.table_name).delete().eq('id', message_id).execute()
            return True if response.data else False

        except Exception as e:
            print(f"Error deleting message from Supabase: {e}")
            return False

    def search_messages(self, search_term: str) -> List[Dict]:
        """
        Search messages by name, email, or message content

        Args:
            search_term (str): The term to search for

        Returns:
            List[Dict]: List of matching message records
        """
        try:
            response = self.client.table(self.table_name).select('*').or_(
                f'name.ilike.%{search_term}%,'
                f'email.ilike.%{search_term}%,'
                f'message.ilike.%{search_term}%'
            ).execute()

            return response.data if response.data else []

        except Exception as e:
            print(f"Error searching messages in Supabase: {e}")
            return []


# Global database instance
_db_instance: Optional[SupabaseDB] = None


def init_db(url: str, key: str) -> SupabaseDB:
    """
    Initialize the global database instance

    Args:
        url (str): Supabase project URL
        key (str): Supabase API key

    Returns:
        SupabaseDB: The initialized database instance
    """
    global _db_instance
    _db_instance = SupabaseDB(url, key)
    return _db_instance


def get_db() -> Optional[SupabaseDB]:
    """
    Get the global database instance

    Returns:
        Optional[SupabaseDB]: The database instance or None if not initialized
    """
    return _db_instance
