import random

random.seed(42)

SBOX = list(range(256))
random.shuffle(SBOX)

INV_SBOX = [0] * 256

for i, value in enumerate(SBOX):
    INV_SBOX[value] = i