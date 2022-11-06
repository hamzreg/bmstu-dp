from bitarray import bitarray
from bitarray.util import ba2int
from dataclasses import dataclass

from encryption.tables import Tables


@dataclass
class Constants:
    change_number = 8


def expanding_permutation(block):
    return bitarray([block[bit - 1] for bit in Tables.expanding_permutation])


def final_permutation(block):
    return bitarray([block[bit - 1] for bit in Tables.final_permutation])


def feistel_cipher(block, key):
    block = expanding_permutation(block)
    z = block ^ key

    result = bitarray()
    i = 0

    for change in range(Constants.change_number):
        row = int(str(z[i:i + 6][0]) + str(z[i:i + 6][5]), 2)
        column = ba2int(z[i + 1:i + 5])

        result.extend(f'{Tables.s[change][row][column]:04b}')

        i += 6

    return final_permutation(result)
