""" Decrypt a path through a Union Route Cipher
Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottomof a column.
Key indicates the orde rto read columns and the direction to traverse.
Negative column numbers means start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed
Arrrows show encryption route; for negative key values read UP.

1 2 3 4

__ __ __ __
|^|||^||| MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START     END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""
import sys

#==============================================================================
# USER INPUT:
# the string to be decrypted(type or paste between triple-quotes)
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

# number of columns in the transposition matrix:
COLS = 4

# number rof rows in the transposition matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex= -1 2 -3 4):
key = """ -1 2 -3 4 """


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#================================================================================

def main():
    """Run program and print decrypted plaintext."""
    print("\nCipher = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key))


    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print("Plaintext = {}".format(plaintext))

