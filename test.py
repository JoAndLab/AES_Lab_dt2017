#!/usr/bin/python3
# -*- coding: utf-8 -*-

import AES256
import readKeyFile
import readBlockFile
import re

key = readKeyFile.getKey('testKey.txt')
filename = 'tWotW.txt'
encrypted_filename = 'encrypted_' + filename
decrypted_filename = 'decrypted_' + filename
open(encrypted_filename, 'w').close()
open(decrypted_filename, 'w').close()


def readPlainText(filename):
    with open(filename, mode='rb') as file:
        while file:
            try:
                s = file.read(16).hex()

                if len(s) == 32:
                    yield [n for n in bytes.fromhex(s)]
                else:
                    length = 32 - len(s)
                    f = 'f' * length
                    s += f
                    yield [n for n in bytes.fromhex(s)]
                    break
            except IOError as e:
                print(e)


def writeEncryptedText(block):
    with open(encrypted_filename, mode='at') as file:
        try:
            file.write(block)
        except IOError as e:
            print(e)


def writeDecryptedText(block):
    with open(decrypted_filename, mode='at', encoding='utf-8', newline='') as file:

        try:
            file.write(block)
        except IOError as e:
            print(e)


def main():
    x = readPlainText(filename)

    for i in x:
        y = AES256.encrypt(i, key)
        z = ''.join([hex(num)[2:].zfill(2) for num in y])

        writeEncryptedText(z)

    test = readBlockFile.getBlock(encrypted_filename)

    for j in test:
        a = AES256.decrypt(j, key)

        b = ''.join([chr(num) for num in a])

        b = "".join(i for i in b if ord(i) < 128)
        b = b.replace('tjL', '')

        writeDecryptedText(b)


if __name__ == '__main__':
    main()
