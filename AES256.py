#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Checkpoint 4-6
# by Anders Mellberg Granat & Johnny Gustavsson

# This is the main file for encrypt and decrypt a text file with AES 256 bit.

# AES info

# The Advanced Encryption Standard (AES), also known as Rijndael(its original name),
# is a specification for the encryption of electronic data established by the
# U.S. National Institute of Standards and Technology (NIST) in 2001.

# AES is based on a design principle known as a substitution-permutation network,
# combination of both substitution and permutation, and is fast in both software and hardware.
# Unlike its predecessor DES, AES does not use a Feistel network. AES is a variant of Rijndael
# which has a fixed block size of 128 bits, and a key size of 128, 192, or 256 bits. By contrast,
# the Rijndael specification per se is specified with block and key sizes that may be any multiple
# of 32 bits, both with a minimum of 128 and a maximum of 256 bits.

# Ref: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

import readKeyFile
import readBlockFile
from keyManager import *
from subBytes import *
from rowShifter import *
from columnMixer import *

from datetime import datetime

key = readKeyFile.getKey('testKey.txt')
filename = 'tWotW.txt'


def file_init(mode):
    """Init definition for file creation"""

    global encrypted_filename
    global decrypted_filename

    if mode == 'ECB':
        encrypted_filename = 'ECB_encrypted_' + filename
        decrypted_filename = 'ECB_decrypted_' + filename
        open(encrypted_filename, 'w').close()
        open(decrypted_filename, 'w').close()
    elif mode == 'CBC':
        encrypted_filename = 'CBC_encrypted_' + filename
        decrypted_filename = 'CBC_decrypted_' + filename
        open(encrypted_filename, 'w').close()
        open(decrypted_filename, 'w').close()


def encrypt(block, key):
    """Definition encrypt a block with key using AES 256 bit"""

    # Init (Key expansion)
    # Round keys are derived from the cipher key using key schedule.
    expanded_key = expandKey(key)

    # 0-th round (add round key)
    # each byte of the state is combined with a block of the round key using bitwise xor.
    block = addRoundKey(block, createRoundKey(expanded_key, 0))

    # 1-th to 13:th round: (rounds)
    for i in range(1, 14):
        block = subBytes(block)  # Substitution step where each byte is replaced with corresponding value from s-box.
        block = shiftRows(block)  # Transposition step where the last three rows in block are shifted.
        block = mixColumns(block)  # Mixing step on the columns of each block, combining the four bytes in each column.
        block = addRoundKey(block, createRoundKey(expanded_key, i))

    # 14:th round (final round)
    block = subBytes(block)
    block = shiftRows(block)
    block = addRoundKey(block, createRoundKey(expanded_key, 14))

    encrypted_block = block

    return encrypted_block


def decrypt(block, key):
    """Definition decrypt a block with key using AES 256 bit"""

    # Initialize
    expanded_key = expandKey(key)

    # 14-th round
    block = addRoundKey(block, createRoundKey(expanded_key, 14))
    block = shiftRowsInv(block)
    block = subBytesInv(block)

    # 13-th to 1:th round:
    for i in range(13, 0, -1):
        block = addRoundKey(block, createRoundKey(expanded_key, i))
        block = mixColumnsInv(block)
        block = shiftRowsInv(block)
        block = subBytesInv(block)

    # 0:th round
    block = addRoundKey(block, createRoundKey(expanded_key, 0))

    decrypted_block = block

    return decrypted_block


def readPlainText(filename):
    """Read plain text as bytes, and yield 16 bytes long blocks of integers (lists)"""

    block_count = 0
    with open(filename, mode='rb') as file:
        while file:
            try:
                block = file.read(16).hex()
                block_count += 1

                if len(block) == 32:
                    yield [n for n in bytes.fromhex(block)]
                else:
                    length = 32 - len(block)
                    padding = '0' * length  # adjust block if shorter then 16 byte (padding)
                    block += padding
                    yield [n for n in bytes.fromhex(block)]
                    break
            except IOError as e:
                print(e)
    print('Block count = ', block_count)  # Prints out how many block the input text contain.


def writeEncryptedText(block):
    """Write encrypted text fo file"""
    with open(encrypted_filename, mode='at') as file:
        try:
            file.write(block)
        except IOError as e:
            print(e)


def writeDecryptedText(block):
    """Write decrypted text fo file"""
    with open(decrypted_filename, mode='at', encoding='utf-8', newline='') as file:

        try:
            file.write(block)
        except IOError as e:
            print(e)


def encryptFile(file, mode):
    """Encrypt file using ECB mode or CBC mode"""

    plain_text = readPlainText(file)

    if mode == 'ECB':

        for i in plain_text:
            block = encrypt(i, key)
            block_as_hex = ''.join([hex(num)[2:].zfill(2) for num in block])

            writeEncryptedText(block_as_hex)
    elif mode == 'CBC':

        iv = [x for x in readBlockFile.getBlock('testBlock.txt')][0]  # Initialization Vector (iv)
        for i in plain_text:
            block = [a ^ b for a, b in zip(iv, i)]
            block = encrypt(block, key)
            block_as_hex = ''.join([hex(num)[2:].zfill(2) for num in block])
            writeEncryptedText(block_as_hex)
            iv = block

    else:
        print('Please choose the encryption mode (ECB or CBC)')


def decryptFile(encrypted_file, mode):
    """Decrypt file using ECB mode or CBC mode"""

    encrypted_block = readBlockFile.getBlock(encrypted_file)

    if mode == 'ECB':

        for i in encrypted_block:
            block = decrypt(i, key)
            block_as_char = ''.join([chr(num) for num in block])
            writeDecryptedText(block_as_char)

    elif mode == 'CBC':

        iv = [x for x in readBlockFile.getBlock('testBlock.txt')][0]

        for i in encrypted_block:
            block = decrypt(i, key)
            block = [a ^ b for a, b in zip(iv, block)]
            block_as_char = ''.join([chr(num) for num in block])
            writeDecryptedText(block_as_char)
            iv = i
    else:
        print('Please choose the decryption mode (ECB or CBC)')


def main():
    mode = 'CBC'  # Sets mode to Electronic Codebook (ECB) or Cipher Block Chaining (CBC)

    file_init(mode)

    print('Encryption starts.. ' + 'mode: ' + mode)

    start_time_encryption = datetime.now()
    encryptFile(filename, mode)
    end_time_encryption = datetime.now()

    encryption_time = end_time_encryption - start_time_encryption

    print('Encryption ends.')
    print('Duration encryption: {}'.format(encryption_time) + '\n')

    print('Decryption starts.. ' + 'mode: ' + mode)

    start_time_decryption = datetime.now()
    decryptFile(encrypted_filename, mode)
    end_time_decryption = datetime.now()

    decryption_time = end_time_decryption - start_time_decryption

    print('Decryption ends.')
    print('Duration decryption: {}'.format(decryption_time))

    print('Duration total: {}'.format(encryption_time + decryption_time))


if __name__ == '__main__':
    main()
