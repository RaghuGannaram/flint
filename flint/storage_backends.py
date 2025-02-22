"""
    flint/storage_backends.py
"""

from storages.backends.s3boto3 import S3Boto3Storage


class S3StaticStorage(S3Boto3Storage):
    """Custom S3 storage for static files."""

    location = "static"
    default_acl = "public-read"  # Publicly readable
    file_overwrite = False  # Prevent overwriting static files
    querystring_auth = False  # No authentication required for static assets


class S3MediaStorage(S3Boto3Storage):
    """Custom S3 storage for media files."""

    location = "media"
    default_acl = "public_read"  # Publicly readable
    file_overwrite = True  # Allow overwriting user-uploaded files
