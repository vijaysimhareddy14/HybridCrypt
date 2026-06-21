from utils import rotate_left
from utils import rotate_right

from sbox import SBOX
from sbox import INV_SBOX


def encrypt(plaintext, round_keys):

    data = bytearray(
        plaintext.encode()
    )

    for r in range(len(round_keys)):

        key = round_keys[r]

        for i in range(len(data)):

            # XOR
            data[i] ^= key[i % len(key)]

            # Rotation
            data[i] = rotate_left(
                data[i],
                r + 1
            )

            # Substitution
            data[i] = SBOX[data[i]]

    return bytes(data)


def decrypt(ciphertext, round_keys):

    data = bytearray(ciphertext)

    for r in reversed(range(len(round_keys))):

        key = round_keys[r]

        for i in range(len(data)):

            # Reverse substitution
            data[i] = INV_SBOX[data[i]]

            # Reverse rotation
            data[i] = rotate_right(
                data[i],
                r + 1
            )

            # Reverse XOR
            data[i] ^= key[i % len(key)]

    return data.decode()