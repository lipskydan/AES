import unittest
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

    out_path = os.path.join(os.path.dirname(file_path), 'encrypted.txt')

    with open(out_path, 'xb') as ff:
        ff.write(bytes(crypted_data))


def t_decrypted(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

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

    out_path = os.path.join(os.path.dirname(file_path), 'decrypted.txt')

    with open(out_path, 'xb') as ff:
        ff.write(bytes(decrypted_data))


class AES_TEST(unittest.TestCase):
    def test_a(self):
        t_encrypt(file_path="input.txt", key="steps")
        t_decrypted(file_path="test/encrypted.txt", key="steps")

        with open("input.txt", 'rb') as f: input = f.read()
        with open("test/decrypted.txt", 'rb') as f: decrypted = f.read()

        self.assertEqual(decrypted, input)
        os.remove("test/decrypted.txt")
        os.remove("test/encrypted.txt")


if __name__ == '__main__':
    unittest.main()
