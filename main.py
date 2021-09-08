import os
import time
import aes

if __name__ == '__main__':

    while True:
        print('press e to encrypt')
        action = input()
        if action not in ['e', 'd']:
            print('Action denied')
            continue
        else:
            break

    while True:
        print('Enter name of file with full path: ')
        file_path = os.path.abspath(input())

        if os.path.isfile(file_path):
            break
        else:
            print('This is not a file')
            continue

    while True:
        print('Enter your Key')
        key = input()

        if len(key) > 16:
            print('Too long Key')
            continue

        for symbol in key:
            if ord(symbol) > 0xff:
                print('Error - maybe you use russian charts - please use english one')
                continue

        break
    print('\r\nprocess is started...')

    time_before = time.time()

    with open(file_path, 'rb') as f:
        data = f.read()

    if action == 'e':
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

        out_path = os.path.join(os.path.dirname(file_path) , 'crypted_' + os.path.basename(file_path))

        with open(out_path, 'xb') as ff:
            ff.write(bytes(crypted_data))