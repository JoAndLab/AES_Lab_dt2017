#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 3
# by Anders Mellberg Granat & Johnny Gustavsson

from sbox import *


def keyScheduleCore(word, iterator):
    """Definition is used as inner loop in key schedule."""

    if len(word) != 4:
        raise RuntimeError('keyScheduleCore() : word size invalid')

    new_word = [sbox[i] for i in word[1:] + word[:1]]  # Applies S-box on all four individual bytes in word.

    new_word[0] = new_word[0] ^ getRconValue(iterator)
    # xor first element in new_word with Rcon value
    # represents the iteration Rcon value.

    return new_word


def expandKey(key):
    """Definition expand a 32 byte key to 240 byte key."""

    expanded_key = list(key)
    key_size = len(expanded_key)
    current_size = key_size
    rcon_iteration = 1

    while current_size < 240:

        temp = expanded_key[-4:]  # Save the last 4 bytes to temp

        if current_size % key_size == 0:
            temp = keyScheduleCore(temp, rcon_iteration)  # Perform keyScheduleCore() on last 4 bytes (temp)
            rcon_iteration += 1

        if current_size % key_size == 16:  # Add extra sbox calculation for 256 bit keys.
            temp = [sbox[i] for i in temp]

        for m in range(4):  # For 256 bit key, this will be repeated 3 times for (m).
            expanded_key.append(expanded_key[current_size - key_size] ^ temp[m])
            current_size += 1
            # Assigns the value of the previous 4 bytes in the expanded key,
            # and xor it with the four-byte block before the new expanded key.
            # This becomes the next 4 bytes in the expanded key

    return expanded_key


def createRoundKey(expanded_key, n):
    """ Creates a round key from the given expanded key and the
        position within the expanded key.
    """
    return expanded_key[(n * 16):(n * 16 + 16)]


def addRoundKey(block, round_key):
    """Definition XOR each element of a roundkey with a block."""
    return [(block[i] ^ round_key[i]) for i in range(0, len(block))]


# Test:

# _word = [0, 1, 2, 3]
# _newWord = keyScheduleCore(_word, 1)
# print(_word)
# print(_newWord)
#
# key = readKeyFile.getKey('testKey.txt')
# exKey = expandKey(key)
# print(exKey)
#
# x0 = createRoundKey(exKey, 0)
# x14 = createRoundKey(exKey, 14)
# print(x0)
# print(x14)

# Test output:

# Input Key:
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
#  17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# word: [0, 1, 2, 3]

# keyScheduleCore(word, 1): [125, 119, 123, 99]

# Expanded key (exKey)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
# 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 165, 115, 194, 159, 161, 118, 196, 152,
# 169, 127, 206, 147, 165, 114, 192, 156, 22, 81, 168, 205, 2, 68, 190, 218, 26,
# 93, 164, 193, 6, 64, 186, 222, 174, 135, 223, 240, 15, 241, 27, 104, 166, 142,
# 213, 251, 3, 252, 21, 103, 109, 225, 241, 72, 111, 165, 79, 146, 117, 248, 235,
# 83, 115, 184, 81, 141, 198, 86, 130, 127, 201, 167, 153, 23, 111, 41, 76, 236,
# 108, 213, 89, 139, 61, 226, 58, 117, 82, 71, 117, 231, 39, 191, 158, 180, 84,
# 7, 207, 57, 11, 220, 144, 95, 194, 123, 9, 72, 173, 82, 69, 164, 193, 135, 28,
# 47, 69, 245, 166, 96, 23, 178, 211, 135, 48, 13, 77, 51, 100, 10, 130, 10, 124,
# 207, 247, 28, 190, 180, 254, 84, 19, 230, 187, 240, 210, 97, 167, 223, 240, 26,
# 250, 254, 231, 168, 41, 121, 215, 165, 100, 74, 179, 175, 230, 64, 37, 65, 254,
# 113, 155, 245, 0, 37, 136, 19, 187, 213, 90, 114, 28, 10, 78, 90, 102, 153, 169,
# 242, 79, 224, 126, 87, 43, 170, 205, 248, 205, 234, 36, 252, 121, 204, 191, 9,
# 121, 233, 55, 26, 194, 60, 109, 104, 222, 54]

# round key position 0 (exKey) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# round key position 14 (exKey) [36, 252, 121, 204, 191, 9, 121, 233, 55, 26, 194, 60, 109, 104, 222, 54]
