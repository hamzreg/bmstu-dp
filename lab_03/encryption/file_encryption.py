from os.path import exists
from os import mkdir
from bitarray import bitarray
from bitarray.util import hex2ba, rindex

from encryption.key_generation import generate_keys
from encryption.des import (
    Constants, 
    padding,
    encipher_block)


def get_file_bits(file_name):
    bits = bitarray()

    with open(file_name, 'rb') as file:
        bits.fromfile(file)

    return bits


def get_key_bits(key):
    key_bits = hex2ba(key)
    zeros = bitarray([0] * (Constants.block_len - len(key_bits)))

    return zeros + key_bits


def write_bits(bits, file_path, deciphering):
    if not deciphering and not exists('cipher/'):
        mkdir('cipher')

    if deciphering and not exists('result/'):
        mkdir('result')

    if deciphering:
        file_path = 'result/result_' + file_path.split('/')[-1]
    else:
        file_path = 'cipher/cipher_' + file_path.split('/')[-1]

    with open(file_path, 'wb') as file:
        bits.tofile(file)


def des_encipher_file(file, deciphering = False):
    key = input('Введите ключ: ')
    key_bits = get_key_bits(key)
    keys = generate_keys(key_bits)

    if deciphering:
        keys.reverse()

    bits = get_file_bits(file)

    if not deciphering:
        bits = padding(bits)

    result = bitarray()

    for i in range(0, len(bits), Constants.block_len):
        result.extend(encipher_block(bits[i:i + Constants.block_len], keys,
                                     deciphering))

    if deciphering:
        result = result[:rindex(result, 1)]

    write_bits(result, file, deciphering)
