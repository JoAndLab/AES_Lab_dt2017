#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 2
# by Anders Mellberg Granat & Johnny Gustavsson


def shiftRows(block):
    """Extract rows as every 4th item starting at [0..3] and move them right as follows:
        row 0, 0 step right
        row 1, 1 step right
        row 2, 2 step right
        row 3, 3 step right
    """

    for i in range(4):
        block[i::4] = block[i::4][i:] + block[i::4][:i]
    return block


def shiftRowsInv(block):
    """Extract rows as every 4th item starting at [0..3] and move them left as follows:
        row 0, 0 step left
        row 1, 1 step left
        row 2, 2 step left
        row 3, 3 step left
    """

    for i in range(4):
        block[i::4] = block[i::4][-i:] + block[i::4][:-i]
    return block

# example shift left [0, 85, 170, 255, 68, 153, 238, 51, 136, 221, 34, 119, 204, 17, 102, 187]
# example shift right [0, 221, 170, 119, 68, 17, 238, 187, 136, 85, 34, 255, 204, 153, 102, 51]
# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
# print(shiftRows(my_list))
