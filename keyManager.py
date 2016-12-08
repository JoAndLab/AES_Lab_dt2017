#!/usr/bin/python3
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
    expanded_key = list(key)
    key_size = len(expanded_key)
    current_size = key_size
    rcon_iteration = 1

    while current_size < 240:

        temp = expanded_key[-4:]  # Save the last 4 bytes to temp

        if current_size % key_size == 0:
            temp = keyScheduleCore(temp, rcon_iteration)  # Perform keyScheduleCore() on last 4 bytes (temp)
            rcon_iteration += 1

        if current_size % key_size == 16:
            temp = [sbox[i] for i in temp]

        for m in range(4):
            expanded_key.append(expanded_key[current_size - key_size] ^ temp[m])
            current_size += 1

    return expanded_key


def createRoundKey(expanded_key, n):
    return expanded_key[(n * 16):(n * 16 + 16)]


# _word = [0, 1, 2, 3]
# _newWord = keyScheduleCore(_word, 1)

# print(_word)
# print(_newWord)

# key = readKeyFile.getKey('testKey.txt')
#
# exKey = expandKey(key)
# print(exKey)
#
# x0 = createRoundKey(exKey, 0)
# x14 = createRoundKey(exKey, 14)
#
# print(x0)
# print(x14)
