#!/usr/bin/python
# -*- coding: utf-8 -*-

import readKeyFile
from sbox import *


def keyScheduleCore(word, iterator):
    if len(word) != 4:
        raise RuntimeError('keyScheduleCore() : word size invalid')

    new_word = [sbox[i] for i in word[1:] + word[:1]]
    new_word[0] = new_word[0] ^ getRconValue(iterator)
    return new_word


def expandKey(key):
    pass


_word = [1, 2, 3, 4]
_newWord = keyScheduleCore(_word, 1)

# print(_word)
# print(_newWord)
