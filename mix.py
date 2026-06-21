def mix_block(block):

    block = bytearray(block)

    for i in range(len(block) - 1):
        block[i] ^= block[i + 1]

    return block


def inverse_mix_block(block):

    block = bytearray(block)

    for i in range(len(block) - 2, -1, -1):
        block[i] ^= block[i + 1]

    return block