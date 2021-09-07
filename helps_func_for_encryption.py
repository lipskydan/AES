from const_tables_and_numbers import nb, nk, nr, sbox, inv_sbox

"""
    inv == False - encryption 
    inv == True - decryption
"""


def sub_bytes(state, inv=False):
    """
    inv == False - encryption (we will use sbox)
    inv == True - decryption (we will use inv_box)
    """

    box = sbox if not inv else inv_sbox

    # if not inv:
    #     box = sbox
    # else:
    #     box = inv_sbox

    for i in range(len(state)):
        for j in range(len(state[i])):
            row = state[i][j] // 0x10
            col = state[i][j] % 0x10

            # Our Sbox is a flat array, not a bable. So, we use this trich to find elem:
            # And DO NOT change list sbox! if you want it to work
            box_elem = box[16 * row + col]
            state[i][j] = box_elem

    return state


def shift_rows(state, inv=False):
    """
    inv == False - encryption (we will use left_shift)
    inv == True - decryption (we will use right_shift)
    """
    count = 1

    if not inv:
        for i in range(1, nb):
            state[i] = left_shift(state[i], count)
            count += 1
    else:
        for i in range(1, nb):
            state[i] = right_shift(state[i], count)
            count += 1

    return state


def left_shift(array, count):
    res = array[:]
    for i in range(count):
        temp = res[1:]
        temp.append(res[0])
        res[:] = temp[:]

    return res


def right_shift(array, count):
    res = array[:]
    for i in range(count):
        tmp = res[:-1]
        tmp.insert(0, res[-1])
        res[:] = tmp[:]

    return res


def mix_columns(state, inv=False):
    pass


def key_expansion(key):
    pass


def add_round_key(state, key_schedule, round=0):
    pass
