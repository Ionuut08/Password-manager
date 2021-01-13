
import hashlib

from itertools import cycle
from random import randint


def encrypt_password(plain_text, password):
    encoded_password = bytes(password, 'utf-8')
    hashed_password = hashlib.md5(encoded_password).hexdigest()
    addition_char = randint(0, 0x100)
    if len(plain_text) > len(hashed_password):
        pwd_iterable = cycle(hashed_password)
    else:
        pwd_iterable = hashed_password
    ret = [chr(((ord(i) ^ ord(j)) + addition_char)) for i, j in zip(plain_text, pwd_iterable)]
    return "".join(reversed(ret)) + chr(addition_char)


def decrypt_password(plain_text, password):
    encoded_password = bytes(password, 'utf-8')
    hashed_password = hashlib.md5(encoded_password).hexdigest()
    addition_char = ord(plain_text[-1])
    if len(plain_text) > len(hashed_password):
        pwd_iterable = cycle(hashed_password)
    else:
        pwd_iterable = hashed_password
    ret = [chr((((ord(i) - addition_char) + 0x100) % 0x100) ^ ord(j)) for i, j in zip(reversed(plain_text[:-1]),
                                                                                      pwd_iterable)]
    return "".join(ret)
