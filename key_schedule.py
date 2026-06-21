import hashlib


def generate_round_keys(key, rounds=12):
    keys = []

    seed = key.encode()

    for i in range(rounds):
        digest = hashlib.sha256(
            seed + str(i).encode()
        ).digest()

        keys.append(digest)

    return keys