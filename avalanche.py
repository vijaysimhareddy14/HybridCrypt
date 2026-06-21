from cipher import encrypt
from key_schedule import generate_round_keys


def count_bit_differences(a, b):

    diff = 0

    for x, y in zip(a, b):

        diff += bin(
            x ^ y
        ).count("1")

    return diff


def avalanche_test(text, key):

    round_keys = generate_round_keys(
        key
    )

    cipher1 = encrypt(
        text,
        round_keys
    )

    modified = list(text)

    modified[0] = chr(
        ord(modified[0]) ^ 1
    )

    modified = "".join(
        modified
    )

    cipher2 = encrypt(
        modified,
        round_keys
    )

    changed_bits = count_bit_differences(
        cipher1,
        cipher2
    )

    total_bits = len(
        cipher1
    ) * 8

    percentage = (
        changed_bits /
        total_bits
    ) * 100

    return (
        changed_bits,
        total_bits,
        percentage
    )