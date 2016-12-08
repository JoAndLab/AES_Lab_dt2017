
# 1. Läsa in
import AES256
import readKeyFile
from codecs import encode

key = readKeyFile.getKey('testKey.txt')


def readText():
    with open('tWotW.txt', mode='rb') as file:
        while file:
            s = file.read(16).hex()
            yield [n for n in bytes.fromhex(s)]

x = readText()

for i in x:
    y = AES256.encrypt(i, key)
    w = ''.join(map(str, y))
    print(w)
