# AES Cipher

### Keywords: 
* State is an intermediate encryption result that can be represented as a rectangular 
byte array with 4 rows and Nb columns. Each State cell contains a 1 byte value. The array State 
is filled with input values. A block of 16 bytes is encrypted at a time.
* Nb is the number of columns (32-bit words) that make up State. For the standard, Nb = 4 is regulated
* Nk is the key length in 32-bit words. For AES, Nk = 4, 6, 8 (I use Nk = 4)
* Nr is the number of encryption rounds. Depending on the key length, Nr = 10, 12 or 14

### Encryption / Decryption Part

#### SubBytes(state, inv)

 The transformation is the replacement of each byte from State with the corresponding one 
 * from the constant table Sbox if we encrypt (inv == False). 
 * from the constant table InvSbox if we decrypt (inv == True).

Each byte from State is represented as {xy} in hexadecimal notation. Then we change each byte
to the element at the intersection of row x and column y.

#### ShiftRows(state, inv=False)

Simple transformation. It performs a cyclic shift:
* to the left if we encrypt (inv == False).
* to the right if we decrypt (inv == True).

Shift 1 item for the first row, 2 for the second and 3 for the third. The zero line is not shifted.

#### MixColumns(state, inv=False)

*Encrypt case (inv == False)*

As part of this transformation, each column in State is represented as a polynomial and multiplied in the
Galois field modulo x4 + 1 with a fixed polynomial 3x^3 + x^2 + x + 2.

*Decrypt case (inv == True)*

The same logic with encrypt case, but we use another fixed polynomial {0b}x^3 + {0d}x^2 + {09}x + {0e}

#### AddRoundKey(state, key_schedule, round=0)

The transformation performs a bitwise XOR of each item from State with the corresponding item from the 
RoundKey array. This method can be used in encryption and decryption part because this transformation is inverse 
of itself due to the properties of the XOR operation: (a XOR b) XOR b = a

*RoundKey - an array of the same size as State, which is built for each round based on the secret key using
the method KeyExpansion()*

#### KeyExpansion(key)

This function generates a set of round keys - KeySchedule. KeySchedule is a long table with 
Nb * (Nr + 1) columns.

*The first round key* is filled in based on the secret key that the user came up with, 
according to the formula KeySchedule [r] [c] = SecretKey [r + 4c], r = 0,1 ... 4; c = 0.1..Nk.

At each iteration, we work with a table column. Columns 0, .., (Nk - 1) are already pre-filled 
with values from the secret word. We start from the column numbered Nk. If the Wi column number
is a multiple of Nk, then we take the Wi-1 column, perform a cyclic left shift over it by one element, 
then replace all the column bytes with the corresponding ones from the Sbox table, 
as we did in SubBytes(). Next, we perform an XOR operation between the Wi-Nk column modified by 
Wi-1 and the Rconi / Nk-1 column. The result is recorded in the Wi column.

For the rest of the columns, XOR between Wi-Nk and Wi-1. We write the result in Wi