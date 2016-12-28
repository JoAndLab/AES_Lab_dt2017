#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 2
# by Anders Mellberg Granat & Johnny Gustavsson

from sbox import *


def subBytes(block):
    """Replace each element value in block with S-box substitute"""
    for i, s in enumerate(block):
        block[i] = getSboxValue(s)
    return block


def subBytesInv(block):
    """Replace each element value in block with inverse S-box substitute"""
    for i, s in enumerate(block):
        block[i] = getSboxInvertValue(s)
    return block

# Test:
#
# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
# print(my_list)
# x = subBytes(my_list)
# print(x)
# y = subBytesInv(x)
# print(y)
#
# Example output:
# original:           [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
# subBytes:           [99, 130, 147, 195, 27, 252, 51, 245, 196, 238, 172, 234, 75, 193, 40, 22]
# subBytes inverse:   [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
