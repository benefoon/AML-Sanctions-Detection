import re

SENSITIVE_FIELDS = ["sender_name", "receiver_name"]

def redact_sensitive_fields(record: dict) -> dict:
    redacted = record.copy()
    for field in SENSITIVE_FIELDS:
        if field in redacted:
            redacted[field] = re.sub(r'[A-Za-z0-9]', '*', redacted[field])
    return redacted
