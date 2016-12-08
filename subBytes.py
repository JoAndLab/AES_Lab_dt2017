#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sbox import *


def subBytes(block):
    for i, s in enumerate(block):
        block[i] = getSboxValue(s)
    return block


def subBytesInv(block):
    for i, s in enumerate(block):
        block[i] = getSboxInvertValue(s)
    return block


# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
#
# print(my_list)
#
# x = subBytes(my_list)
#
# print(x)
#
# y = subBytesInv(x)
#
# print(y)
