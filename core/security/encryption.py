from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

KEY = os.getenv("AES_KEY", "").encode()  # 32-byte key (AES-256)

def encrypt_field(plain_text: str) -> str:
    iv = get_random_bytes(12)
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=iv)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
    return base64.b64encode(iv + tag + ciphertext).decode()

def decrypt_field(encrypted_text: str) -> str:
    data = base64.b64decode(encrypted_text)
    iv, tag, ciphertext = data[:12], data[12:28], data[28:]
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=iv)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()
