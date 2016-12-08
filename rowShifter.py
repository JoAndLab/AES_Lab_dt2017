#!/usr/bin/python3
# -*- coding: utf-8 -*-


def shiftRows(block):
    # Extract rows as every 4th item starting at [1..3]

    for i in range(4):
        block[i::4] = block[i::4][i:] + block[i::4][:i]
    return block


def shiftRowsInv(block):
    # Extract rows as every 4th item starting at [1..3]

    for i in range(4):
        block[i::4] = block[i::4][-i:] + block[i::4][:-i]
    return block


# ex shift left [0, 85, 170, 255, 68, 153, 238, 51, 136, 221, 34, 119, 204, 17, 102, 187]


# ex shift right [0, 221, 170, 119, 68, 17, 238, 187, 136, 85, 34, 255, 204, 153, 102, 51]

# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
#
# print(shiftRows(my_list))
