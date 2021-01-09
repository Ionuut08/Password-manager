
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes


def encrypt_password(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return b64encode(cipher_text).decode('utf-8')


def decrypt_password(enc_dict, password):
    # decode the dictionary entries from base64
    salt = '/T7Qb1nzDaT3nqlwoeLU/w=='
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = 'CdzGO/l26viorBwmslmLlg=='
    tag = '/T7Qb1nzDaT3nqlwoeLU/w=='

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


def main():
    password = 'master'

    encrypted = encrypt("verygoodpassword", password)
    print(encrypted)

    decrypted = decrypt(encrypted, password)
    print(decrypted)


if __name__ == '__main__':
    main()