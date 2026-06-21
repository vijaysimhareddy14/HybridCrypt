from utils import rotate_left
from utils import rotate_right

from sbox import SBOX
from sbox import INV_SBOX

from permutation import (
    permute_block,
    inverse_permute_block
)


BLOCK_SIZE = 8


def encrypt(plaintext, round_keys):

    data = bytearray(
        plaintext.encode()
    )

    while len(data) % BLOCK_SIZE:
        data.append(0)

    for r in range(len(round_keys)):

        key = round_keys[r]

        for i in range(len(data)):

            data[i] ^= key[i % len(key)]

            data[i] = rotate_left(
                data[i],
                r + 1
            )

            data[i] = SBOX[data[i]]

        for start in range(
            0,
            len(data),
            BLOCK_SIZE
        ):

            block = data[
                start:start + BLOCK_SIZE
            ]

            data[
                start:start + BLOCK_SIZE
            ] = permute_block(block)

    return bytes(data)


def decrypt(ciphertext, round_keys):

    data = bytearray(ciphertext)

    for r in reversed(
        range(len(round_keys))
    ):

        for start in range(
            0,
            len(data),
            BLOCK_SIZE
        ):

            block = data[
                start:start + BLOCK_SIZE
            ]

            data[
                start:start + BLOCK_SIZE
            ] = inverse_permute_block(
                block
            )

        key = round_keys[r]

        for i in range(len(data)):

            data[i] = INV_SBOX[
                data[i]
            ]

            data[i] = rotate_right(
                data[i],
                r + 1
            )

            data[i] ^= key[
                i % len(key)
            ]

    return data.rstrip(
        b"\x00"
    ).decode()