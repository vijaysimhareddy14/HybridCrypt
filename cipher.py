from utils import rotate_left
from utils import rotate_right


def encrypt(plaintext, round_keys):

    data = bytearray(
        plaintext.encode()
    )

    for r in range(len(round_keys)):

        key = round_keys[r]

        for i in range(len(data)):

            data[i] ^= key[i % len(key)]

            data[i] = rotate_left(
                data[i],
                (r + 1)
            )

    return bytes(data)


def decrypt(ciphertext, round_keys):

    data = bytearray(ciphertext)

    for r in reversed(range(len(round_keys))):

        key = round_keys[r]

        for i in range(len(data)):

            data[i] = rotate_right(
                data[i],
                (r + 1)
            )

            data[i] ^= key[i % len(key)]

    return data.decode()