import hashlib

def hash_entity(entity_name: str) -> str:
    return hashlib.sha256(entity_name.lower().strip().encode('utf-8')).hexdigest()
