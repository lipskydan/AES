import os
import time

import aes

# 2b7e151628aed2a6

if __name__ == '__main__':

    while True:
        print('Press:\n e for encription \n d for decription\nInput choice: ')
        action_name = input()
        if action_name not in ['e', 'd']:
            print('Action denied')
            continue
        else:
            break
    print()

    while True:
        print('Enter name of file with full path')
        file_path = os.path.abspath(input())

        if os.path.isfile(file_path):
            break
        else:
            print('This is not a file')
            continue
    print()

    while True:
        print('Enter your key')
        key = input()

        if len(key) > 16:
            print('Error - too long key')
            continue

        for symbol in key:
            if ord(symbol) > 0xff:
                print('Error - use only latin alphabet and numbers')
                continue

        break

    print('AES is working, please wait....')

    time_before = time.time()

    with open(file_path, 'rb') as f:
        data = f.read()

    if action_name == 'e':
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

        out_path = os.path.join(os.path.dirname(file_path), 'crypted_' + os.path.basename(file_path))

        with open(out_path, 'xb') as ff:
            ff.write(bytes(crypted_data))

    else:
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

        out_path = os.path.join(os.path.dirname(file_path), 'decrypted_' + os.path.basename(file_path))

        with open(out_path, 'xb') as ff:
            ff.write(bytes(decrypted_data))

    time_after = time.time()

print('New file here:', out_path, '-- working time is ', time_after - time_before, ' seconds')