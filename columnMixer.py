#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mixColTables import *


def mixColumn(col):
    g0, g1, g2, g3 = galois_normal
    c0, c1, c2, c3 = col

    return (g0[c0] ^ g1[c1] ^ g2[c2] ^ g3[c3],
            g3[c0] ^ g0[c1] ^ g1[c2] ^ g2[c3],
            g2[c0] ^ g3[c1] ^ g0[c2] ^ g1[c3],
            g1[c0] ^ g2[c1] ^ g3[c2] ^ g0[c3])


def mixColumnInv(col):
    g0, g1, g2, g3 = galois_inverse
    c0, c1, c2, c3 = col

    return (g0[c0] ^ g1[c1] ^ g2[c2] ^ g3[c3],
            g3[c0] ^ g0[c1] ^ g1[c2] ^ g2[c3],
            g2[c0] ^ g3[c1] ^ g0[c2] ^ g1[c3],
            g1[c0] ^ g2[c1] ^ g3[c2] ^ g0[c3])


def mixColumns(block):
    # Perform mixColumn for each column in the block
    for i, j in (0, 4), (4, 8), (8, 12), (12, 16):
        block[i:j] = mixColumn(block[i:j])

    return block


def mixColumnsInv(block):
    # Perform mixColumnInv for each column in the block
    for i, j in (0, 4), (4, 8), (8, 12), (12, 16):
        block[i:j] = mixColumnInv(block[i:j])

    return block

# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
#
# print(my_list)
#
# x = mixColumns(my_list)
#
# print(x)
#
# y = mixColumnsInv(x)
#
# print(y)
