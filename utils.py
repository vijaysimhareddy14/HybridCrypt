def rotate_left(byte, shift):
    shift %= 8
    return ((byte << shift) & 0xFF) | (byte >> (8 - shift))


def rotate_right(byte, shift):
    shift %= 8
    return ((byte >> shift) | (byte << (8 - shift))) & 0xFF