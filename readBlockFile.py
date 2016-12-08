#!/usr/bin/python3
# -*- coding: utf-8 -*-


def getBlock(filename):
    with open(filename, 'r') as f:
        while f:
            try:
                my_block = f.read(32)
                if len(my_block) == 32:
                    yield [n for n in bytes.fromhex(my_block)]
                else:
                    length = 32 - len(my_block)
                    f = 'f' * length
                    my_block += f
                    yield [n for n in bytes.fromhex(my_block)]
                    break
            except IOError:
                print('Cannot read file')
