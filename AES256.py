#!/usr/bin/python3
# -*- coding: utf-8 -*-

from readKeyFile import *
from readBlockFile import *
from keyManager import *
from addRoundKey import *
from subBytes import *
from rowShifter import *
from columnMixer import *


def encrypt(block, key):

    # Initialize
    expanded_key = expandKey(key)

    # 0-th round
    block = addRoundKey(block, createRoundKey(expanded_key, 0))

    # 1-th to 13:th round:
    for i in range(1, 14):
        block = subBytes(block)
        block = shiftRows(block)
        block = mixColumns(block)
        block = addRoundKey(block, createRoundKey(expanded_key, i))

    # 14:th round
    block = subBytes(block)
    block = shiftRows(block)
    block = addRoundKey(block, createRoundKey(expanded_key, 14))

    encrypted_block = block

    return encrypted_block


def decrypt(block, key):

    # Initialize
    expanded_key = expandKey(key)

    # 14-th round
    block = addRoundKey(block, createRoundKey(expanded_key, 14))
    block = shiftRowsInv(block)
    block = subBytesInv(block)

    # 13-th to 1:th round:
    for i in range(13, 0, -1):
        block = addRoundKey(block, createRoundKey(expanded_key, i))
        block = mixColumnsInv(block)
        block = shiftRowsInv(block)
        block = subBytesInv(block)

    # 0:th round
    block = addRoundKey(block, createRoundKey(expanded_key, 0))

    decrypted_block = block

    return decrypted_block


def main():
    key = getKey('testKey.txt')
    block = getBlock('testBlock.txt')

    encrypted_block = encrypt(block, key)
    decrypted_block = decrypt(encrypted_block, key)

    print(block)
    print(encrypted_block)
    print(decrypted_block)


if __name__ == '__main__':
    main()
