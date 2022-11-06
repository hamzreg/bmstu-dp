from bitarray import bitarray
from dataclasses import dataclass

from encryption.key_generation import generate_keys
from encryption.feistel import feistel_cipher
from encryption.tables import Tables


@dataclass
class Constants:
    block_len = 64
    rounds_number = 16


def padding(data):
    data.append(1)
    zeros = [0] * (Constants.block_len - len(data) % Constants.block_len)
    data.extend(zeros)

    return data


def initial_permutation(input_block):
    return bitarray([input_block[bit - 1] for bit in Tables.initial_permutation])


def final_permutation(input_block):
    result_block = bitarray([0] * Constants.block_len)
    
    for index, bit in enumerate(Tables.initial_permutation):
        result_block[bit - 1] = input_block[index]

    return result_block


def encipher_block(block, keys, deciphering):
    block = initial_permutation(block)
    left, right = block[:32], block[32:]

    if deciphering:
        left, right = right, left

    for round in range(Constants.rounds_number):
        left, right = right, left ^ feistel_cipher(right, keys[round])

    if deciphering:
        left, right = right, left

    return final_permutation(left + right)
