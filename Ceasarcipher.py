"""
Author: Christopher Duncan
Build Date: 01/21/2022
This is a python build for the ceasar cipher algorithm. This algorithm is a simple and easy method of encryption.
It is primarily a substitution cipher. Each letter of plain text is replaced by a letter with some fixed number of
positions down the alphabet.

Resources Utilized:
https://medium.com/vacatronics/caesar-cipher-in-python-98d06e98989d
https://www.youtube.com/watch?v=JEsUlx0Ps9k
https://www.youtube.com/watch?v=pIt4Q68J00A

"""
import string

plaintext = "hello world"
shift = 7

alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

"""Starting at the position shift then taking the rest 
of the list, then append everything that came before shift. ex if shift was 2 code means

alphabet[shift:] == ABCDEFG --> CDEFGAB  # Next we make a translation table."""

""" This means were putting the alphabet and the shifted one on top of 
# each other."""
table = str.maketrans(alphabet, shifted_alphabet)

encrypted = plaintext.translate(table)

print(encrypted)







