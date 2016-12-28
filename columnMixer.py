#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 2
# by Anders Mellberg Granat & Johnny Gustavsson

from mixColTables import *


def mixColumn(col):
    """ Definition mix column by the formula
        b0 = 2a0 + 3a1 + 1a2 + 1a3
        b1 = 1a0 + 2a1 + 3a2 + 1a3
        b2 = 1a0 + 1a1 + 2a2 + 3a3
        b3 = 3a0 + 1a1 + 1a2 + 2a3
        (+ = xor)
        using galois tables.
    """

    g0, g1, g2, g3 = galois_normal
    c0, c1, c2, c3 = col

    return (g0[c0] ^ g1[c1] ^ g2[c2] ^ g3[c3],
            g3[c0] ^ g0[c1] ^ g1[c2] ^ g2[c3],
            g2[c0] ^ g3[c1] ^ g0[c2] ^ g1[c3],
            g1[c0] ^ g2[c1] ^ g3[c2] ^ g0[c3])


def mixColumnInv(col):
    """Definition mix column reverse by formula
        a0 = 14b0 + 11b1 + 13b2 + 9b3
        a1 = 9b0 + 14b1 + 11b2 + 13b3
        a2 = 13b0 + 9b1 + 14b2 + 11b3
        a3 = 11b0 + 13b1 + 9b2 + 14b3
        (+ = xor)
        using galois tables"""
    g0, g1, g2, g3 = galois_inverse
    c0, c1, c2, c3 = col

    return (g0[c0] ^ g1[c1] ^ g2[c2] ^ g3[c3],
            g3[c0] ^ g0[c1] ^ g1[c2] ^ g2[c3],
            g2[c0] ^ g3[c1] ^ g0[c2] ^ g1[c3],
            g1[c0] ^ g2[c1] ^ g3[c2] ^ g0[c3])


def mixColumns(block):
    """Perform mixColumn for each column in the block"""
    for i, j in (0, 4), (4, 8), (8, 12), (12, 16):
        block[i:j] = mixColumn(block[i:j])

    return block


def mixColumnsInv(block):
    """Perform mixColumnInv for each column in the block"""
    for i, j in (0, 4), (4, 8), (8, 12), (12, 16):
        block[i:j] = mixColumnInv(block[i:j])

    return block

# test:
#
# my_list = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
# print(my_list)
# x = mixColumns(my_list)
# print(x)
# y = mixColumnsInv(x)
# print(y)
#
# example output:
#
# original:       [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
# mixed:          [34, 119, 0, 85, 102, 51, 68, 17, 170, 255, 136, 221, 238, 187, 204, 153]
# mixed inverse:  [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
