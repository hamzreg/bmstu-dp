from bitarray import bitarray
from dataclasses import dataclass

from encryption.tables import Tables


@dataclass
class Constants:
    rounds_number = 16


def initial_permutation(key):
    return bitarray([key[bit - 1] for bit in Tables.key_initial_permutation])


def left_shift(key, offset):
    end = key[:offset]
    key <<= offset

    return key[:-offset] + end


def contraction_permutation(key):
    return bitarray([key[bit - 1] for bit in Tables.contraction_permutation])


def generate_keys(key):
    key = initial_permutation(key)
    c, d = key[:28], key[28:]

    keys = []

    for round in range(Constants.rounds_number):
        c = left_shift(c, Tables.shift[round])
        d = left_shift(d, Tables.shift[round])

        keys.append(contraction_permutation(c + d))

    return keys
