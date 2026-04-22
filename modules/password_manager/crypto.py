import os
from typing import Tuple

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


SALT_SIZE = 16
NONCE_SIZE = 12
ITERATIONS = 200_000


def derive_key(master_password: str, salt: bytes) -> bytes:
    """Derive a 256-bit key from master password."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    return kdf.derive(master_password.encode())


def encrypt_password(
    master_password: str, plaintext: str
) -> Tuple[bytes, bytes, bytes]:
    """
    Encrypt a password using AES-256-GCM.

    Returns:
        ciphertext, salt, nonce
    """
    salt = os.urandom(SALT_SIZE)

    key = derive_key(master_password, salt)

    nonce = os.urandom(NONCE_SIZE)

    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)

    return ciphertext, salt, nonce


def decrypt_password(
    master_password: str, ciphertext: bytes, salt: bytes, nonce: bytes
) -> str:
    """
    Decrypt a password using AES-256-GCM.
    """
    key = derive_key(master_password, salt)

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    return plaintext.decode()
