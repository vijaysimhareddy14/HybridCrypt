PERMUTATION = [
    7, 2, 5, 0,
    6, 1, 4, 3
]

INV_PERMUTATION = [0] * 8

for i, pos in enumerate(PERMUTATION):
    INV_PERMUTATION[pos] = i


def permute_block(block):

    result = bytearray(8)

    for i in range(8):
        result[i] = block[PERMUTATION[i]]

    return result


def inverse_permute_block(block):

    result = bytearray(8)

    for i in range(8):
        result[i] = block[INV_PERMUTATION[i]]

    return result