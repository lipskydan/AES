import unittest
from asyncio import sleep

import aes
import os


def t_encrypt(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    crypted_data = []
    temp = []

    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            crypted_part = aes.encrypt(temp, key)
            crypted_data.extend(crypted_part)
            del temp[:]
    else:

        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            crypted_part = aes.encrypt(temp, key)
            crypted_data.extend(crypted_part)

    return  crypted_data


def t_decrypted(data, key):
    # with open(file_path, 'rb') as f:
    #     data = f.read()

    decrypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            decrypted_part = aes.decrypt(temp, key)
            decrypted_data.extend(decrypted_part)
            del temp[:]
    else:

        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            decrypted_part = aes.decrypt(temp, key)
            decrypted_data.extend(decrypted_part)

    return decrypted_data


class AES_TEST(unittest.TestCase):
    def test_a(self):
        with open("input.txt", 'rb') as f:
            data = f.read()
        i = []
        for byte in data:
            i.append(byte)
        e = t_encrypt(file_path="input.txt", key="steps")
        d = t_decrypted(data=e, key="steps")
        del d[len(i):len(d)]
        self.assertEqual(i, d)


if __name__ == '__main__':
    unittest.main()
