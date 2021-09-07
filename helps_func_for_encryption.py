"""
    inv == False - encryption 
    inv == True - decryption
"""


def sub_bytes(state, inv=False):
    """
    inv == False - encryption (we will use sbox)
    inv == True - decryption (we will use inv_box)
    """
    pass


def shift_rows(state, inv=False):
    """
    inv == False - encryption (we will use left_shift)
    inv == True - decryption (we will use right_shift)
    """
    pass


def left_shift(array, count):
    pass


def right_shift(array, count):
    pass


def mix_columns(state, inv=False):
    pass


def key_expansion(key):
    pass


def add_round_key(state, key_schedule, round=0):
    pass
