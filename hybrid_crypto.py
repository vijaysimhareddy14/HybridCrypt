import secrets

from cipher import encrypt
from cipher import decrypt

from key_schedule import generate_round_keys

from rsa import (
    encrypt_rsa,
    decrypt_rsa
)


def generate_session_key():

    return secrets.token_hex(16)


def hybrid_encrypt_file(
    input_file,
    output_file,
    public_key
):

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as f:

        plaintext = f.read()

    session_key = generate_session_key()

    round_keys = generate_round_keys(
        session_key
    )

    encrypted_data = encrypt(
        plaintext,
        round_keys
    )

    encrypted_session_key = encrypt_rsa(
        session_key,
        public_key
    )

    with open(
        output_file,
        "w"
    ) as f:

        f.write(
            ",".join(
                map(
                    str,
                    encrypted_session_key
                )
            )
        )

        f.write("\n")

        f.write(
            encrypted_data.hex()
        )

    print(
        "Hybrid encryption complete."
    )


def hybrid_decrypt_file(
    input_file,
    output_file,
    private_key
):

    with open(
        input_file,
        "r"
    ) as f:

        lines = f.readlines()

    encrypted_key = list(
        map(
            int,
            lines[0].strip().split(",")
        )
    )

    cipher_hex = lines[1].strip()

    session_key = decrypt_rsa(
        encrypted_key,
        private_key
    )

    round_keys = generate_round_keys(
        session_key
    )

    plaintext = decrypt(
        bytes.fromhex(cipher_hex),
        round_keys
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(plaintext)

    print(
        "Hybrid decryption complete."
    )