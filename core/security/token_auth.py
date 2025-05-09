from fastapi import Request, HTTPException
from typing import Set
from functools import lru_cache
import os
import secrets

# Load and cache valid tokens from secure environment
@lru_cache()
def get_valid_tokens() -> Set[str]:
    return set(os.getenv("VALID_API_TOKENS", "").split(","))

def verify_token_signature(token: str) -> bool:
    # Add signature validation logic if JWT/HMAC used
    return token in get_valid_tokens()

async def verify_token(request: Request):
    token = request.headers.get("X-API-Token")
    if not token or not verify_token_signature(token):
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid or missing token.")
