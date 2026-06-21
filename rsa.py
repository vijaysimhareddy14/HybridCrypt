import random
from math import gcd


def mod_inverse(e, phi):

    def extended_gcd(a, b):

        if a == 0:
            return b, 0, 1

        g, x1, y1 = extended_gcd(
            b % a,
            a
        )

        x = y1 - (b // a) * x1
        y = x1

        return g, x, y

    _, x, _ = extended_gcd(
        e,
        phi
    )

    return x % phi


def generate_keys():

    p = 61
    q = 53

    n = p * q

    phi = (
        (p - 1)
        *
        (q - 1)
    )

    e = 17

    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(
        e,
        phi
    )

    public_key = (
        e,
        n
    )

    private_key = (
        d,
        n
    )

    return (
        public_key,
        private_key
    )


def encrypt_rsa(message, public_key):

    e, n = public_key

    encrypted = []

    for ch in message:

        encrypted.append(
            pow(
                ord(ch),
                e,
                n
            )
        )

    return encrypted


def decrypt_rsa(cipher, private_key):

    d, n = private_key

    text = ""

    for value in cipher:

        text += chr(
            pow(
                value,
                d,
                n
            )
        )

    return text