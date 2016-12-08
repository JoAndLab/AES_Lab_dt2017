#!/usr/bin/python3
# -*- coding: utf-8 -*-


def getKey(filename):
    my_key = ''
    with open(filename, 'r') as f:
        try:
            my_key = f.readline()
        except IOError:
            print('Cannot read file')

    return [n for n in bytes.fromhex(my_key)]


