from cipher import encrypt
from cipher import decrypt

from key_schedule import generate_round_keys


def encrypt_file(input_file, output_file, key):

    round_keys = generate_round_keys(key)

    with open(input_file, "r", encoding="utf-8") as f:
        plaintext = f.read()

    encrypted = encrypt(
        plaintext,
        round_keys
    )

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(
        f"Encrypted file saved as {output_file}"
    )


def decrypt_file(input_file, output_file, key):

    round_keys = generate_round_keys(key)

    with open(input_file, "rb") as f:
        encrypted = f.read()

    plaintext = decrypt(
        encrypted,
        round_keys
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(plaintext)

    print(
        f"Decrypted file saved as {output_file}"
    )