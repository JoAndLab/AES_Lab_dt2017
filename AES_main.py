#!/usr/bin/python
# -*- coding: utf-8 -*-

import readKeyFile
import readBlockFile
from sbox import *


my_key_list = readKeyFile.getKey('testKey.txt')
print(my_key_list)

my_block_list = readBlockFile.getBlock('testBlock.txt')
print(my_block_list)

print(getSboxValue(0))
print(getSboxInvertValue(0))
print(getRconValue(0))


def main():
    pass


if __name__ == '__main__':
    main()

