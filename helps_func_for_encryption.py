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
    for i in range(nb):

        if not inv:  # encryption
            s0 = mul_by_02(state[0][i]) ^ mul_by_03(state[1][i]) ^ state[2][i] ^ state[3][i]
            s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(state[2][i]) ^ state[3][i]
            s2 = state[0][i] ^ state[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(state[3][i])
            s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(state[3][i])
        else:  # decryption
            s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
            s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
            s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
            s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

    return state


def mul_by_02(num):
    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b

    return res % 0x100


def mul_by_03(num): return mul_by_02(num) ^ num
def mul_by_09(num): return mul_by_02(mul_by_02(mul_by_02(num))) ^ num
def mul_by_0b(num): return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num
def mul_by_0d(num): return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num
def mul_by_0e(num): return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)


def key_expansion(key):
    pass


def add_round_key(state, key_schedule, round=0):
    for col in range(nk):
        # nb*round is a shift which indicates start of a part of the KeySchedule
        s0 = state[0][col] ^ key_schedule[0][nb * round + col]
        s1 = state[1][col] ^ key_schedule[1][nb * round + col]
        s2 = state[2][col] ^ key_schedule[2][nb * round + col]
        s3 = state[3][col] ^ key_schedule[3][nb * round + col]

        state[0][col] = s0
        state[1][col] = s1
        state[2][col] = s2
        state[3][col] = s3

    return state
