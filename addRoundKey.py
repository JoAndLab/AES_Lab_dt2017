#!/usr/bin/python3
# -*- coding: utf-8 -*-


def addRoundKey(block, round_key):
    return [(block[i] ^ round_key[i]) for i in range(0, len(block))]
