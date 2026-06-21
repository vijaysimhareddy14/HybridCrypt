import hashlib


def generate_round_keys(key, rounds=8):
    seed = key.encode()

    keys = []

    for i in range(rounds):
        digest = hashlib.sha256(
            seed + str(i).encode()
        ).digest()

        keys.append(digest)

    return keys