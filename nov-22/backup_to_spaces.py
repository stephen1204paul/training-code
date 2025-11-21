#!/usr/bin/env python3
"""
Automated backup script for Digital Ocean Spaces
Backs up specified directories to object storage
"""

import boto3
import os
import tarfile
from datetime import datetime
from botocore.client import Config

# Configuration - UPDATE THESE VALUES
SPACES_KEY = 'YOUR_ACCESS_KEY'
SPACES_SECRET = 'YOUR_SECRET_KEY'
SPACES_REGION = 'sgp1'  # e.g., nyc3, sfo3, sgp1
SPACES_BUCKET = 'my-training-bucket'
SPACES_ENDPOINT = f'https://{SPACES_REGION}.digitaloceanspaces.com'

# Directories to backup
BACKUP_DIRS = [
    '/var/www/html',
    '/etc/nginx'
]

# Temporary directory for archive
TEMP_DIR = '/tmp'

def create_spaces_client():
    """Create and return a Spaces client"""
    session = boto3.session.Session()
    client = session.client(
        's3',
        region_name=SPACES_REGION,
        endpoint_url=SPACES_ENDPOINT,
        aws_access_key_id=SPACES_KEY,
        aws_secret_access_key=SPACES_SECRET,
        config=Config(signature_version='s3v4')
    )
    return client

def create_backup_archive():
    """Create a compressed archive of backup directories"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f'backup_{timestamp}.tar.gz'
    archive_path = os.path.join(TEMP_DIR, archive_name)

    print(f"Creating archive: {archive_name}")

    with tarfile.open(archive_path, 'w:gz') as tar:
        for directory in BACKUP_DIRS:
            if os.path.exists(directory):
                print(f"  Adding: {directory}")
                tar.add(directory, arcname=os.path.basename(directory))
            else:
                print(f"  Warning: {directory} not found, skipping")

    return archive_path, archive_name

def upload_to_spaces(client, file_path, object_name):
    """Upload file to Spaces"""
    print(f"Uploading to Spaces: {object_name}")

    try:
        client.upload_file(
            file_path,
            SPACES_BUCKET,
            f'backups/{object_name}'
        )
        print(f"Successfully uploaded to: backups/{object_name}")
        return True
    except Exception as e:
        print(f"Error uploading: {e}")
        return False

def list_backups(client):
    """List existing backups in Spaces"""
    print("\nExisting backups:")

    try:
        response = client.list_objects_v2(
            Bucket=SPACES_BUCKET,
            Prefix='backups/'
        )

        if 'Contents' in response:
            for obj in response['Contents']:
                size_mb = obj['Size'] / (1024 * 1024)
                print(f"  - {obj['Key']} ({size_mb:.2f} MB)")
        else:
            print("  No backups found")

    except Exception as e:
        print(f"Error listing backups: {e}")

def cleanup_old_backups(client, keep_count=5):
    """Remove old backups, keeping only the most recent ones"""
    print(f"\nCleaning up old backups (keeping {keep_count} most recent)...")

    try:
        response = client.list_objects_v2(
            Bucket=SPACES_BUCKET,
            Prefix='backups/'
        )

        if 'Contents' in response:
            # Sort by last modified date
            backups = sorted(
                response['Contents'],
                key=lambda x: x['LastModified'],
                reverse=True
            )

            # Delete old backups
            for backup in backups[keep_count:]:
                print(f"  Deleting: {backup['Key']}")
                client.delete_object(
                    Bucket=SPACES_BUCKET,
                    Key=backup['Key']
                )

    except Exception as e:
        print(f"Error cleaning up: {e}")

def main():
    print("=" * 50)
    print("Digital Ocean Spaces Backup Script")
    print("=" * 50)

    # Create Spaces client
    client = create_spaces_client()

    # Create backup archive
    archive_path, archive_name = create_backup_archive()

    # Upload to Spaces
    success = upload_to_spaces(client, archive_path, archive_name)

    # Clean up local archive
    if os.path.exists(archive_path):
        os.remove(archive_path)
        print(f"Cleaned up local archive: {archive_path}")

    # List and cleanup old backups
    if success:
        list_backups(client)
        cleanup_old_backups(client, keep_count=5)

    print("\nBackup complete!")
    print("=" * 50)

if __name__ == '__main__':
    main()
