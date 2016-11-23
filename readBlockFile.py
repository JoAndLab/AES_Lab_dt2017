#!/usr/bin/python
# -*- coding: utf-8 -*-


def getBlock(filename):
    my_block = ''
    with open(filename, 'r') as f:
        try:
            my_block = f.readline()
        except IOError:
            print('Cannot read file')

    return [n for n in bytes.fromhex(my_block)]
