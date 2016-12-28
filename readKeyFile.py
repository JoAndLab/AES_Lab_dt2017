#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 1
# by Anders Mellberg Granat & Johnny Gustavsson


def getKey(filename):
    """ This definition reads a 32 byte key from file"""

    my_key = ''
    with open(filename, 'r') as f:
        try:
            my_key = f.readline()
        except IOError:
            print('Cannot read file')

    if len(my_key) != 64:
        print('Key must be 32 byte long (hex string length 64)')
    else:
        return [n for n in bytes.fromhex(my_key)]

        # Example return:
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        # 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
