"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "HDB_ADDRESS": env("HDB_ADDRESS", "f4a3724b752e.hana.us10.hanacloud.com"),
    "HDB_PORT": env("HDB_PORT", 443),
    "HDB_USER": env("HDB_USER", "USER_HDI_DB_1"),
    "HDB_PASSWORD": env("HDB_PASSWORD", "password123"),
    "HDB_SCHEMA": env("HDB_SCHEMA", "SCHEMA_HDI_DB_1"),
    "HDB_TABLE": env("HDB_TABLE", "TABLE"),
    "HDB_HEADERS": env("HDB_HEADERS", ""),
    "LABELS": env("LABELS", "")
}
