# AES Cipher

### Keywords: 
* State is an intermediate encryption result that can be represented as a rectangular 
byte array with 4 rows and Nb columns. Each State cell contains a 1 byte value. The array State 
is filled with input values. A block of 16 bytes is encrypted at a time.
* Nb is the number of columns (32-bit words) that make up State. For the standard, Nb = 4 is regulated
* Nk is the key length in 32-bit words. For AES, Nk = 4, 6, 8. We have already decided that we will use Nk = 4
*Nr is the number of encryption rounds. Depending on the key length, Nr = 10, 12 or 14

### Encryption Part

We can illustrate encryption part by next scheme:

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

#### AddRoundKey(state, key_schedule, round=0)

#### KeyExpansion(key)




