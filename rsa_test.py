from rsa import (
    generate_keys,
    encrypt_rsa,
    decrypt_rsa
)

public_key, private_key = generate_keys()

print(
    "Public:",
    public_key
)

print(
    "Private:",
    private_key
)

message = "HELLO"

cipher = encrypt_rsa(
    message,
    public_key
)

print(
    "Encrypted:",
    cipher
)

plain = decrypt_rsa(
    cipher,
    private_key
)

print(
    "Decrypted:",
    plain
)