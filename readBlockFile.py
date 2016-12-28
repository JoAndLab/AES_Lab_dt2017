#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 1
# by Anders Mellberg Granat & Johnny Gustavsson


def getBlock(filename):
    """ This definition reads a 16 byte block from plain text
    as an object, yields 16 byte long list of integers. """

    with open(filename, 'r') as f:
        while f:
            try:
                my_block = f.read(32)
                if len(my_block) == 32:
                    yield [n for n in bytes.fromhex(my_block)]
                else:
                    break
            except IOError:
                print('Cannot read file')

# Example of yield list: [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
