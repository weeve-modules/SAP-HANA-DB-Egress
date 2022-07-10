from os import getenv

PARAMS = {
    "HDB_ADDRESS": getenv("HDB_ADDRESS", "f4a3724b752e.hana.us10.hanacloud.com"),
    "HDB_PORT": int(getenv("HDB_PORT", 443)),
    "HDB_USER": getenv("HDB_USER", "USER_HDI_DB_1"),
    "HDB_PASSWORD": getenv("HDB_PASSWORD", "password123"),
    "HDB_SCHEMA": getenv("HDB_SCHEMA", "SCHEMA_HDI_DB_1"),
    "HDB_TABLE": getenv("HDB_TABLE", "TABLE"),
    "HDB_HEADERS": getenv("HDB_HEADERS", ""),
    "LABELS": getenv("LABELS", "")
}
