#!/usr/bin/python3
# -*- coding: utf-8 -*-

from keyManager import *
from addRoundKey import *
from readKeyFile import *
from readBlockFile import *
from sbox import *

my_key_list = getKey('testKey.txt')
print(my_key_list)

my_block_list = getBlock('testBlock.txt')
print(my_block_list)

print(getSboxValue(0))
print(getSboxInvertValue(0))
print(getRconValue(0))

print('\n\n')

expandedKey = expandKey(my_key_list)
roundKey0 = createRoundKey(expandedKey, 0)

addedRoundKeyToBlock = addRoundKey(my_block_list, roundKey0)

print(addedRoundKeyToBlock)


def main():
    pass


if __name__ == '__main__':
    main()
